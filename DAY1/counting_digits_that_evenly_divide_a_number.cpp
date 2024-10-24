#include<bits/stdc++.h>
using namespace std;

int evenlyDivides(int N){
    //Code here
    int dup_N = N;
    int count = 0;
    int lastDigit;
    
    while(N != 0){
        lastDigit = N % 10;
        if (dup_N % lastDigit == 0){
            count++;
        }
        N = N / 10;
    }
    return count;
}

int main(){
    int num = 14;
    int op = evenlyDivides();
    cout << op << endl;

    return 0;
}

