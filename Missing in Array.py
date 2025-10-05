int missingNum(int *arr, int size) {
    int n = size + 1;
    int xor1 = 0, xor2 = 0;

    // XOR all array elements
    for (int i = 0; i < size; i++) {
        xor2 ^= arr[i];
    }

    // XOR all numbers from 1 to n
    for (int i = 1; i <= n; i++) {
        xor1 ^= i;
    }

    return xor1 ^ xor2;
}
