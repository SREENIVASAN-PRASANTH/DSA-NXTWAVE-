#include <bits/stdc++.h>
using namespace std;

int main() {
    int divisorCount = 0;
    int number = 5;
    
    for(int i = 1;i <= sqrt(number);i++){
        if(number % i == 0){
            divisorCount++;
            if (i != (number/i)){
                divisorCount++;
            }
            
        }
    }
    // cout << sqrt(number) << endl;
    // cout << divisorCount << endl;
    if (divisorCount == 2){
        cout << "It is a prime number" << endl;
    }
    else{
        cout << "It is not a prime number" << endl;
    }

    return 0;
}

// time complexity = O(sqrt(number))