#include <iostream>
using namespace std;

int LinearSearch(int arr[],int size, int key)
{
    for(int i=0; i<size; i++)
    {
        if(arr[i]==key)
        return i;
    }
    cout<<"Target Value Not found in the Array"<<endl;
    return -1;
}

int main() {
     int arr[10]={435,2,376,29,68,293,44,2,1,6};
     for(int i:arr)
     cout<<i<<"\t";
     cout<<endl;
     int key;
     cout<<"Enter the Target Value:-\t";
     cin>>key;
     int index=LinearSearch(arr,10,key);
     if(index!=-1)
     cout<<"Target Value Founded At the index:-\t"<<index;
}