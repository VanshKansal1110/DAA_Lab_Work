#include <iostream>
using namespace std;

void missing_num(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == size)
        {
            continue;
        }
        if (arr[i] != i)
        {
            int temp = arr[arr[i]];
            arr[arr[i]] = arr[i];
            arr[i] = temp;
            i--;
        }
    }
    int i = 0;
    while (arr[i] == i)
        i++;
    if (i < size)
        cout << "Missing Value Is:-\t" << i << endl;
    else
        cout << "No Element Missing" << endl;
}

int main()
{
    int size;
    cout << "Enter the Number of the Elements:-\t";
    cin >> size;
    int *arr = new int[size];
    cout << "Enter the " << size << " Elements for arr" << endl;
    for (int i = 0; i < size; i++)
    {
        int temp;
        cin >> temp;
        if (temp > size || temp < 0)
        {
            cout << "Value is not valid enter the number between 0 And " << size << " (Including both), Not More than that.\nEnter Value Again\n";
            i--;
            continue;
        }
        arr[i] = temp;
    }
    cout << "Entered Array:-\n";
    for (int i = 0; i < size; i++)
        cout << arr[i] << "\t";
    cout<<endl;
    missing_num(arr, size);
}