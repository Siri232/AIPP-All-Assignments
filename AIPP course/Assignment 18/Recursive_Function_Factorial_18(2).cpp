#include <iostream>

// Recursive function to calculate factorial
int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    std::cout << "--- C++ Factorial Calls ---" << std::endl;
    std::cout << "Enter a non-negative integer to calculate its factorial: ";
    int numToFactorialize;
    std::cin >> numToFactorialize;

    if (numToFactorialize < 0) {
        std::cout << "Factorial is not defined for negative numbers." << std::endl;
    } else {
        std::cout << "Factorial of " << numToFactorialize << " = " << factorial(numToFactorialize) << std::endl;
    }
    return 0;
}

