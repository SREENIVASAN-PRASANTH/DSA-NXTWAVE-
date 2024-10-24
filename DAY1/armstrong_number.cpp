#include <bits/stdc++.h>
using namespace std;

int armstrongNumber(int num){
    int copyNum = num;
    int sum = 0;
    int lenNumber = 0;

    while(copyNum != 0){
        lenNumber = lenNumber + 1;
        copyNum = copyNum / 10;
    }

    copyNum = num;

    while(copyNum != 0){
        int lastDigit = copyNum % 10;
        sum = sum + pow(lastDigit,lenNumber);
        copyNum = copyNum / 10;
    }

    if (num == sum){
        return 1;
    }

    else{
        return 0;
    }
}

int main(){

    int op = armstrongNumber(1);

    if(op == 1){
        cout << "it is a armstrong number" << endl;
    }
    else{
        cout << "not a armstrong number" << endl;
    }
    return 0;
}