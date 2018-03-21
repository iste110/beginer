// C++ program to find missing k numbers
// in an array.
#include <bits/stdc++.h>
using namespace std;
 
// Prints first k natural numbers in
// arr[0..n-1]
void printKMissing(int arr[], int n, int k)
{
    sort(arr, arr + n);
 
    // Find first positive number
    int i = 0;
    while (i < n && arr[i] <= 0)
        i++;
 
    // Now find missing numbers
    // between array elements
    int count = 0, curr = 1;
    while (count < k && i < n) {
        if (arr[i] != curr) {
            cout << curr << " ";
            count++;
        } else
            i++;
 
        curr++;
    }
 
    // Find missing numbers after
    // maximum.
    while (count < k) {
        cout << curr << " ";
        curr++;
        count++;
    }
}
 
// Driver code
int main()
{
    int arr[] = { 2, 3, 4 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;
    printKMissing(arr, n, k);
    return 0;
}
