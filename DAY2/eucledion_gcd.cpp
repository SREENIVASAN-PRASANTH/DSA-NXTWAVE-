#include <bits/stdc++.h>
using namespace std;

int gcd(int num1,int num2){
    while(num1 != 0 && num2 != 0){
        if(num1 >= num2){
            num1 = num1 % num2;
        }
        else{
            num2 = num2 % num1;
        }
    }
    
    if(num1 == 0){
        return num2;
    }
    else{
        return num1;
    }
}

int main() {
    int op = gcd(2,10);
    cout << op << endl;
    return 0;
}

// time complexity = O(log(min(a,b)))