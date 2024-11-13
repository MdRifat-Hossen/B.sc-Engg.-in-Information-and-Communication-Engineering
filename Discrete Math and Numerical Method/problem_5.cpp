#include<bits/stdc++.h>
using namespace std;
int main()
{
    
    int n,m;
    cin>>n>>m;
    int m1[n][m];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
           cin>>m1[i][j];
        }
    }
    int m2[n][m];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
           cin>>m2[i][j];
        }
    }
    int Union[n][m];
    int Inter[n][m];
    cout<<"Union (m1 ∪  m2):"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<" |"<<" ";
        for(int j=0;j<m;j++)
        {
            Union[i][j]=m1[i][j] || m2[i][j];
            cout<<Union[i][j]<<" ";
        }
         cout<<"|"<<endl;
    }
     cout<<"Intersection (m1 ∩ m2):"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<" |"<<" ";
        for(int j=0;j<m;j++)
        {
            Inter[i][j]=m1[i][j] && m2[i][j];
            cout<<Inter[i][j]<<" ";
        }
        cout<<"|"<<endl;
    }
   
    return 0;
}
