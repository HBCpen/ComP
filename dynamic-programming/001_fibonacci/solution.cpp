#include <iostream>

int fib(int n) {
    if (n <= 1) {
        return n;
    }
    int a = 0, b = 1;
    for (int i = 2; i <= n; ++i) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    int n = 10;
    std::cout << "The " << n << "th Fibonacci number is: " << fib(n) << std::endl;
    return 0;
}
