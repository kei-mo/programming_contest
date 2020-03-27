#include <bits/stdc++.h>
using namespace std;

int main(){
    long long a,b,k;
    long long ans_a,ans_b;
    cin>>a >> b>> k;
    if (a-k<0)
    {
        ans_a = 0;
        if (b-(k-a)<0)
        {
            ans_b = 0;
        } else {
            ans_b = b-(k-a);
        }
    } else
    {
        ans_a = a-k;
        ans_b = b;
    }

    cout<<ans_a<<" "<<ans_b<<endl;
}

