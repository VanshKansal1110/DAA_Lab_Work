#include <iostream>
using namespace std;

int BinarySearch(int *arr, int key, int s, int e)
{
    if (s > e)
        return -1;
    int m = (s + e) / 2;
    if (arr[m] == key)
        return m;
    else if (arr[m] > key)
        return BinarySearch(arr, key, s, m - 1);
    else
        return BinarySearch(arr, key, m + 1, e);
}

int main()
{
    int arr[10]={1,2,3,77,88,96,943,5555,9999,10000};

    cout<<endl<<"Array:-"<<endl;
    for (int i = 0; i < 10; i++)
        cout << arr[i] << "\t";
    int key;
    cout << endl
         << "----------------------------------------------" << endl
         << "Enter the Value of the target value to Find:-\t";
    cin >> key;
    int index = BinarySearch(arr, key, 0, 9);
    if (index != -1)
        cout << "The Target value " << key << " is Found At the Index:-\t" << index;
    else
    cout<<"Target Value Not Found In the Array.";
}