#include <bits/stdc++.h>
using namespace std;

int main() {
    int N = 4;
    
    for(int i = 1;i <= N;i++){
        for(int j = N - i + 1;j >= 1;j--){
            cout << "*" << " ";
        }
        cout << endl;
    }
    

    return 0;
}