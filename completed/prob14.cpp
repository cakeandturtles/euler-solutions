#include <iostream>
using namespace std;

int main()
{
    string junk;
    unsigned int count, j;
    unsigned int whichNum;
    unsigned int maxCount=0;
    for (unsigned int i=999168; i>0; i--)
    {
        count=0;
        j=i;
        while (j!=1)
        {
            count++;
            if (j<=0)
            {
                cout << "ERROR OVERFLOW!\n";
                return 1;
            }
            if (j%2==0)
                j = j/2;
            else
                j=(3*j)+1;
        }
        if (count>maxCount)
        {
            maxCount = count;
            whichNum = i;
        }
    }
    cout << whichNum << endl;
    return 0;
}
