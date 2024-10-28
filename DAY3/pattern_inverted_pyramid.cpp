#include <bits/stdc++.h>
using namespace std;

int main() {
    int N = 4;
    int stars = N + (N - 1);
    
    for(int i = 1;i <= N;i++){
        // for printing spaces using this loop
        for(int k = 1;k <= i - 1;k ++){
            cout << "  ";
        }
        
        //for printing stars using this loop
        for(int j = stars;j >= 1;j--){
            cout << "*" << " ";
        }
        
        //decrementing two stars for each loop
        stars = stars - 2;
        cout << endl;
    }
    

    return 0;
}