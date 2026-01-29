#include <iostream>
using namespace std;

void selection_sort(int *(arr), int size)
{
    if(size<2)
    return;
    for(int i=1; i<size; i++)
    {
        if(arr[0]>arr[i])
        {   
            swap(arr[0], arr[i]);
        }
    }
    selection_sort(++arr, size-1);
}

int main() {
    int arr[10]={435,2,376,29,68,293,44,2,1,6};
    for(int i : arr)
    cout<<i<<"\t";
    cout<<endl;
    selection_sort(arr, 10);
    for(int i : arr)
    cout<<i<<"\t";
}