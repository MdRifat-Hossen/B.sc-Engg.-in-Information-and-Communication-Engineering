#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    cout<<"Find Relation R1:"<<endl;
    cout<<"R1"<<"="<<"{";
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(a[j] % a[i] == 0)
            {
                   cout<<"("<<a[i]<<","<<a[j]<<"),";
            }
        }
    }
    cout<<"}"<<endl;
   
    cout<<"Find Relation R2:"<<endl;
      cout<<"R2"<<"="<<"{";
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(a[i] <= a[j])
            {
                   cout<<"("<<a[i]<<","<<a[j]<<"),";
            }
        }
    }
    cout<<"}";
    return 0;
}
