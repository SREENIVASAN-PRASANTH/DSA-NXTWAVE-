#include <bits/stdc++.h>
using namespace std;

int main() {
    int num1 = 14;
    int num2 = 18;
    int min;
    if(num1 > num2){
        min = num2;
    }
    else{
        min = num1;
    }
    
    int gcd = 1;
    
    for(int i = 1;i <= min;i++){
        if((num1 % i) == 0 && (num2 % i) == 0){
            gcd = i;
        }
    }
    
    cout << gcd << endl;
    return 0;
}

// time complexity = O(min(A,B))