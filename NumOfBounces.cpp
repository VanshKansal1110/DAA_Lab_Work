#include <iostream>
using namespace std;

int numOfBounces(float vel)
{
    if(vel<=1)
    return 0;
    return 1+numOfBounces(vel*0.425);
}

int main() {
    float vel;
    cout<<"Enter the Velocity(in m/sec) of the ball with which it hits the ground:-\t";
    cin>>vel;
    cout<<"Number of the Bounces:-\t"<<numOfBounces(vel);
}