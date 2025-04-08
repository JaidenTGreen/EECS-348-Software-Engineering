// Matrix.hpp - Header file defining a templated Matrix class

#ifndef MATRIX_HPP
#define MATRIX_HPP

#include <iostream>   // for std::cin, std::cout
#include <vector>     // for std::vector

// Define a Matrix class using a template to support both int and double types
template <typename T>
class Matrix {
private:
    int size;  // Size of the matrix (N for N x N)
    std::vector<std::vector<T> > data;  // 2D vector to store matrix elements

public:
    // Constructor to initialize matrix with given size
    Matrix(int n) : size(n), data(n, std::vector<T>(n)) {}

    // Default constructor
    Matrix() : size(0) {}

    // Function to return the size of the matrix
    int getSize() const { return size; }

    // Overload input operator >>
    friend std::istream& operator>>(std::istream& in, Matrix<T>& matrix) {
        // Loop through each row
        for (int i = 0; i < matrix.size; i++) {
            // Loop through each column
            for (int j = 0; j < matrix.size; j++) {
                in >> matrix.data[i][j];  // Read value into matrix
            }
        }
        return in;
    }

    // Overload output operator <<
    friend std::ostream& operator<<(std::ostream& out, const Matrix<T>& matrix) {
        for (int i = 0; i < matrix.size; i++) {
            for (int j = 0; j < matrix.size; j++) {
                out << matrix.data[i][j] << "\t";  // Print value with tab spacing
            }
            out << std::endl;  // New line after each row
        }
        return out;
    }

    // Overload addition operator
    Matrix<T> operator+(const Matrix<T>& other) const {
        Matrix<T> result(size);  // Create a new result matrix
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                result.data[i][j] = this->data[i][j] + other.data[i][j];  // Add elements
            }
        }
        return result;  // Return the resulting matrix
    }

    // Overload multiplication operator
    Matrix<T> operator*(const Matrix<T>& other) const {
        Matrix<T> result(size);  // Result matrix
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                result.data[i][j] = 0;  // Initialize cell
                for (int k = 0; k < size; k++) {
                    result.data[i][j] += data[i][k] * other.data[k][j];  // Multiply and accumulate
                }
            }
        }
        return result;  // Return product matrix
    }

    // Get diagonal sums
    T sumDiagonals() const {
        T sum = 0;
        for (int i = 0; i < size; i++) {
            sum += data[i][i];             // Main diagonal
            sum += data[i][size - 1 - i];  // Secondary diagonal
        }
        return sum;
    }

    // Swap two rows
    void swapRows(int r1, int r2) {
        if (r1 >= 0 && r2 >= 0 && r1 < size && r2 < size)
            std::swap(data[r1], data[r2]);  // Swap entire row vectors
    }

    // Swap two columns
    void swapCols(int c1, int c2) {
        if (c1 >= 0 && c2 >= 0 && c1 < size && c2 < size) {
            for (int i = 0; i < size; i++) {
                std::swap(data[i][c1], data[i][c2]);  // Swap individual column values
            }
        }
    }

    // Update a specific element
    void update(int row, int col, T value) {
        if (row >= 0 && col >= 0 && row < size && col < size)
            data[row][col] = value;  // Update the cell
    }
};

#endif
