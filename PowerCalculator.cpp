#include <iostream>
using namespace std;

float power(int num , int pow)
{
    if(pow==0)
    return 1;
    if(pow==1)
    return num;
    if(pow>1)
    {
        if(pow%2==0)
            return power(num*num, pow/2);
        else
            return num*power(num*num, (pow-1)/2);
    }
    else
    {
        return 1/(float)power(num, pow*(-1));
    }
}

int main() {
    int num,pow;
    cout<<"Enter the Number and Its Power:-\n";
    cin>>num>>pow;
    cout<<endl;
    cout<<"Result of the "<<num<<"^"<<pow<<"\t=\t"<<power(num, pow);

}