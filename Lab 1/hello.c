//A sample C program. It reads a string of characters and prints its letters in (1)
//capitalized letters, and (2) in reverse order of the letters.
#include <stdio.h>
#include <string.h>
int main() {
 char str[100];
 int i, len;
 printf("Enter a string: ");
 gets(str);
 len = strlen(str);
 for (i = 0; i < len; i++) {
 if (str[i] >= 'a' && str[i] <= 'z') {
 str[i] = str[i] - 'a' + 'A';
 }
 }
 printf("The capitalized string is: %s\n", str);
 // Reverse the string.
 for (i = 0, len = strlen(str); i < len / 2; i++) {
 char temp = str[i];
 str[i] = str[len - 1 - i];
 str[len - 1 - i] = temp;
 }
 printf("The reversed string is: %s\n", str);
 return 0;
}
//If the program is entered correctly and it compiles, then you may run it (assuming
//its name is string-pgm) to get an output like this:
