#include <iostream>
using namespace std;

int sum_n_nums(int *arr, int n)
{
    if(n!=0)
    return arr[0]+sum_n_nums(++arr, n-1);
    return 0;
}

int main() {
    int arr[10]={3,4,634,24,75,24,75,12,53,88}, sum;
    sum= sum_n_nums(arr, 10);
    cout<<sum;
}