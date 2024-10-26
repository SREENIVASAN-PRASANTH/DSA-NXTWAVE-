#include <bits/stdc++.h>
using namespace std;


int main() {
    int num1 = 2;
    int num2 = 3;
    int lcm = num1 * num2;
    
    int max;
    if(num1 < num2){
        max = num2;
    }
    else{
        max = num1;
    }
    
    for(int i = max; i <= num1 * num2;i ++){
        if(i % num1 == 0 && i % num2 == 0){
            lcm = i;
            cout << lcm << endl;
        }
    }
}