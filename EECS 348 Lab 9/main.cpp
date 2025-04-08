// main.cpp - Driver to test Matrix class

#include <iostream>    // For I/O
#include <fstream>     // For file I/O
#include "Matrix.hpp"  // Include our matrix class

int main() {
    std::ifstream infile("matrix_input.txt");  // Open input file
    int n, type;
    infile >> n >> type;  // Read size and type

    if (type == 0) {
        Matrix<int> A(n), B(n);  // Create int matrices
        infile >> A >> B;        // Read matrix data
        std::cout << "Matrix A:\n" << A;
        std::cout << "Matrix B:\n" << B;

        std::cout << "\nA + B:\n" << (A + B);
        std::cout << "\nA * B:\n" << (A * B);

        std::cout << "\nDiagonal Sum of A: " << A.sumDiagonals() << std::endl;

        A.swapRows(0, 1);  // Swap rows
        std::cout << "\nA after swapping row 0 and 1:\n" << A;

        A.swapCols(0, 1);  // Swap columns
        std::cout << "\nA after swapping col 0 and 1:\n" << A;

        A.update(0, 0, 99);  // Update element
        std::cout << "\nA after updating (0,0) to 99:\n" << A;

    } else {
        Matrix<double> A(n), B(n);  // Create double matrices
        infile >> A >> B;           // Read matrix data
        std::cout << "Matrix A:\n" << A;
        std::cout << "Matrix B:\n" << B;

        std::cout << "\nA + B:\n" << (A + B);
        std::cout << "\nA * B:\n" << (A * B);

        std::cout << "\nDiagonal Sum of A: " << A.sumDiagonals() << std::endl;

        A.swapRows(0, 1);
        std::cout << "\nA after swapping row 0 and 1:\n" << A;

        A.swapCols(0, 1);
        std::cout << "\nA after swapping col 0 and 1:\n" << A;

        A.update(0, 0, 3.14);
        std::cout << "\nA after updating (0,0) to 3.14:\n" << A;
    }

    return 0;  // End of program
}
