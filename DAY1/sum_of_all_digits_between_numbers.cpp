#include<bits/stdc++.h>
using namespace std;

int calculateDigitSum(int N1, int N2)
{
    //Code here
    int sum = 0;
    for(int i = N1;i <= N2;i ++){
        int dupI = i;
        while(dupI != 0){
            sum += (dupI % 10);
            dupI = dupI/10;
        }
    }
    return sum;
}

int main(){
    int op = calculateDigitSum(13,17);
    cout << op << endl;

    return 0;
}