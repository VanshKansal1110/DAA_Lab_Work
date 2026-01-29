#include <iostream>
using namespace std;

void permutation(string str, int s, int e)
{
    if (s == e)
    {
        cout << str << endl;
        return;
    }
    for(int i=s; i<e; i++)
    {
        swap(str[s], str[i]);
        permutation(str,s+1,e);
    }
}

int main()
{
    string str = "123";
    permutation(str, 0, str.size());
}