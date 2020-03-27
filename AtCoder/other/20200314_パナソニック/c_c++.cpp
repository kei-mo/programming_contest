#include <bits/stdc++.h>
using namespace std;
 
int main() {
    double a,b,c,d;
    cin >> a;
    cin >> b;
    cin >> c;
    d = a*a + b*b + c*c -2*a*b -2*a*c - 2*b*c;
 if (d >0) {
    cout << "Yes" << endl;
  }
  else {
    cout << "No" << endl;
  }
}