#include <iostream>
#include <cassert>

// http://vivi.dyndns.org/blog/archives/354

using namespace std;

int bitCount(int number) {
    int counter = 0;

    for (int i = 1; i > 0; i <<= 1) {
        if (number & i) counter++;
    }

    return counter;
}

int bitCountReverse(int number) {
    assert(number >= 0); // If number is negative, it cannot count the number of 1
    int counter = 0;

    for (; number > 0; number >>= 1) {
        counter += number & 1;
    }
    return counter;
}

int bitCountRemoving(int number) {
    int counter = 0;

    for (; number != 0; number = number & (number - 1)) {
        counter++;
    }
    return counter;
}

int main() {
    cout << bitCount(7) << endl;
    cout << bitCountReverse(7) << endl;
    cout << bitCountRemoving(7) << endl;
    return 0;
}