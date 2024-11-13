#include<bits/stdc++.h>
using namespace std;
int main()
{
    
    int n;
    cin>>n;
    int a[n];
    for(int i =0;i<n;i++)
    {
        cin>>a[i];
    }
    int m;
    cin>>m;
    int b[m];
    for(int j=0;j<m;j++)
    {
        cin>>b[j];
    }
    int r[n][m];
    cout<<"Find Relation"<<endl;
    cout<<"R={";
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(a[i] > b[j])
            {
                cout<<"("<<a[i]<<","<<b[j]<<"),";
                r[i][j]=1;
            }
            else
            {
                r[i][j]=0;
            }
        }
    }
    cout<<"}"<<endl;
    cout<<"print matrix"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<" |"<<" ";
        for(int j=0;j<m;j++)
        {
            cout<<r[i][j]<<" ";
        }
         cout<<"|"<<endl;
    }
    return 0;
}
