#include <iostream>

int f(int x) {
    while (x < 10000000) {
        x += 13;
    }
    return x - 3;
}

int main() {
    int n;
    std::cin >> n;
    std::cout << f(n) << "\n";
    return 0;
}
