#include <iostream>
using namespace std;

void insertionSort(int *arr, int size)
{
    for (int i = 1; i < size; i++)
    {
        for (int j = i - 1; j >= 0; j--)
        {
            if (arr[j] > arr[j+1])
            {
                swap(arr[j], arr[j + 1]);
                continue;
            }
            break;
        }
    }
}

int main()
{
    int size;
    cout << "Enter the Size of the Array:-\t";
    cin >> size;
    int *arr = new int[size];

    cout << "Enter the Array Elements:-\n";
    for (int i = 0; i < size; i++)
        cin >> arr[i];
    cout << endl
         << "--------------------------------------------" << endl
         << "Entered the Array:-\n";
    for (int i = 0; i < size; i++)
        cout << arr[i] << "\t";
    cout << endl;
    insertionSort(arr, size);
    cout << endl
         << "--------------------------------------------" << endl
         << "Array After Sorting:-\n";
    for (int i = 0; i < size; i++)
        cout << arr[i] << "\t";
}