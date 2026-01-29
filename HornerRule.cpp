#include <iostream>
using namespace std;

int HornerRule(int deg, int x, int *arr)
{
    if(deg==0)
    return arr[0];
    return (HornerRule(deg-1,x,arr)*x)+arr[deg];
}

int main() {
    int degree=3, x=-2;
    int arr[4]={1, -3, 3, -1};
    cout<<HornerRule(degree, x, arr);   
    
}