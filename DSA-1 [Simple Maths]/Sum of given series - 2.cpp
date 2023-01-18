// https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_MATH_NEW/ME_PE_SIMPLE_MATH_NEW_MODULE_SERIESSUMII/assessment/

#include <bits/stdc++.h>
using namespace std;

// TODO: Implement this method
double seriesSumII(double A, double R){
    return A / (1 - R);
}

// NOTE: Please do not modify this function
int main(){
    double A, R;
    cin >> A >> R;
    double result = seriesSumII(A, R);
    cout << fixed << result;
}
