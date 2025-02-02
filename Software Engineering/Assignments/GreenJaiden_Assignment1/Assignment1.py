'''
Name: EECS 348 Assignment 1
Description: CEO Email Prioritization Program
Inputs: Assignment1_Text_File.txt
Outputs: Next email and number of unread emails
Collaborators: Jaiden Green
Sources: Youtube, ChatGPT
Author: Jaiden Green
Creation Date: 1/30/25
'''

from datetime import datetime

#Creates MaxHeap Class (For sorting)
#MaxHeap Class from Programming and Math Totorials on youtube
#https://www.youtube.com/watch?v=GnKHVXv_rlQ
#used ChatGPT to debug
class MaxHeap:
    def __init__(self, items=[]):                   #can receive items to insert into the heap
        super().__init__()
        self.heap = []                              #Creates a new list with a value of 0 at index 0
        for i in items:                             #For loop to insert items into the list
            self.heap.append(i)                     #appends elements one at a time
            self.__floatUp(len(self.heap) - 1)      #floats the elements to their position in the tree

    def push(self, data):                       #Push function that takes in data
        self.heap.append(data)                  #Appends data to the end of the heap
        self.__floatUp(len(self.heap) - 1)      #Floats data up to it's proper position

    def peek(self):                 #peek function
        if len(self.heap) > 1:      #checks first value on the list
            return self.heap[1]     #returns first value on the list
        else:                       #return for if heap is empty
            return False    
        
    def pop(self):                                  #pop function
        if len(self.heap) > 1:                      #checks if heap has two or more values
            self.__swap(0, len(self.heap) - 1)      #swaps the first and last values of the heap 
            max = self.heap.pop()                   #pops the next value off the heap
            self.__bubbleDown(0)                    #bubbles down value in position 1 to it's real value
        elif len(self.heap) == 1:       #if there is only one value on heap
            max = self.heap.pop()       #sets value to max
        else:                           #trying to pop a value off an empty heap
            max = False                 #returns false
        return max                      #returns output of pop

    def __swap(self, i, j):             #swap function, replaces the heap index with the second called variable
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2                           #finds the parent index
        if index <= 1:                              #checks if index is one
            return
        elif self.heap[index] > self.heap[parent]:  #if index is greater than parent
            self.__swap(index, parent)              #swaps the two variables
            self.__floatUp(parent)                  #recurses until in position

    def __bubbleDown(self, index):
        left = index * 2                    #identifies left child index
        right = index * 2 + 1               #odentifies right child index
        largest = index                     #sets the largest index to the current one
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left                  #compares left child and sets to largest if it is
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right                 #compares right child and sets to largest if it is
        if largest != index:                #if the largest is not the index
            self.__swap(index, largest)     #swaps index and largest
            self.__bubbleDown(largest)      #bubbles down the largest to it's true value (recursive)

#ChatGPT helped with getting ideas and creation of the Email class
class Email:                    #class for functions that'll be used in processing emails
    def __init__(self):         #initializes class
        self.heap = MaxHeap()   #operator to use MaxHeap
        self.count = 0          #counting operator

    priority = {                #mapping of priorized emails
        "Boss ": 5,             #Boss set to 5 (highest)
        "Subordinate": 4,       #Sub set to 4
        "Peer": 3,              #Peer set to 3
        "ImportantPerson": 2,   #Important set to 2
        "OtherPerson": 1        #Other set to 1 (lowest)
    }

    def add_email(self, sender, subject, date): #function to add emails to heap based on priority
        if sender not in self.priority:         #if a sender isn't in the priority mapping
            return                              #ignores sender
        
        
        date_obj = datetime.strptime(date, "%m-%d-%Y")  #converts the date (string) into datetime (object)
        time = int(date_obj.timestamp())                #converts datetime into a timestamp

        self.heap.push((self.priority[sender], time, self.count, sender, subject, date)) #pushes a tuple into the heap
        self.count += 1                                                                  #First in, first out order for the heap

    def next_email(self):                       #shows the next email, doesn't destroy it
        if len(self.heap.heap) == 0:            #if the heap is empty
            print("No emails to read.")         #outputs that there were no emails
            return
        email = self.heap.peek()                #calls for the highest-priority email
        if email:                               #if there's an email
            print("\nNext email:")              #formatting
            print(f"  Sender: {email[3]}")      #prints sender info
            print(f"  Subject: {email[4]}")     #prints subject info
            print(f"  Date: {email[5]}")        #prints date

    def read_email(self):                       #removes recent email, and displays new heap
        if len(self.heap.heap) == 0:            #if there's nothing in the heap
            print("No emails to read.")         #tells user
            return
        email = self.heap.pop()                 #Remove highest-priority email
        if email:                               #if theres an email
            print("\nNext email:")              #formatting
            print(f"  Sender: {email[3]}")      #prints sender info
            print(f"  Subject: {email[4]}")     #prints subject info
            print(f"  Date: {email[5]}")        #prints date

    def count_emails(self):                     #shows number of unread emails
        print(f"\nThere are {len(self.heap.heap)} emails to read.")

def processing(commands):               #function for processing the input file
    email_manager = Email()             #stores an email
    
    try:
        with open(filename, 'r') as file:       #reads in an inputted file
            for line in file:                   #reads each line one at a time
                command = line.strip()          #strips each line
                if not command:                 #if there's empty lines
                    continue                    #ignores empty lines
                
                parts = command.split(" ", 1)   #split command type and data
                action = parts[0]               #new variable for parts at the first iterable
                
                if action == "EMAIL":                               #if statement for action calls, for email action
                    email_data = parts[1].split(",")                #splits line to get sender, sugject, date
                    sender = email_data[0].strip()                  #cleans sender text
                    subject = email_data[1].strip()                 #cleans subject text
                    date = email_data[2].strip()                    #cleans date text
                    email_manager.add_email(sender, subject, date)  #calls func, adds email to heap
                
                elif action == "NEXT":              #for next action
                    email_manager.next_email()      #runs next email operator
                
                elif action == "READ":              #for read action
                    email_manager.read_email()      #runs read email operator
                
                elif action == "COUNT":             #for count action
                    email_manager.count_emails()    #runs count emails operator

    except FileNotFoundError:                                   #if there's no found file
        print(f"Error: The file '{filename}' was not found.")   #tells the user

filename = "Assignment1_Test_File.txt" #stores file in a variable, change this to your file name if it's not the same
processing(filename)    #runs the program / processor
