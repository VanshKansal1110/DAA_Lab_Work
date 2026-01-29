#include <iostream>
using namespace std;

int count=1;
void TOH(int num, char f, char u, char t)
{
    if(num>0)
    {
        TOH(num-1, f,t,u);
        cout<<"Step-"<<count++<<"->\t Move From Plate-"<<f<<" To Plate-"<<t<<endl;
        TOH(num-1,u,f,t);
    }
}

int main()
{
    int num;
    cout << "Enter the Number of the Plates:-\t";
    cin >> num;
    cout << "\n\n\tLet the Plates Are in the \t'A' Stack.\n\tWe need to transfer it to the \t'C' Stack." << endl
         << "\tWe have the \t'B' Stack \tempty To Use For the Transfer of the plates.\n\n" << endl
         << " Steps to Follow to Transfer plates from 'A->C:- '\n";
    TOH(num, 'A', 'B','C');
}