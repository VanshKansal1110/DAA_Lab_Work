#include <iostream>
using namespace std;

int firstDuplicateIndex(int *arr, int size)
{
    for(int i=0; i<(size/2); i++)
    {
        for(int j=0; j<i;j++)
        {
            if(arr[j]==arr[i])
            return i;
        }
    }
    return (size/2);
}

int main() {
    int arr[6]={1,5,1,2,5,2};
    cout<<firstDuplicateIndex(arr,6);
}