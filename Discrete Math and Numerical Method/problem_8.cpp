#include<bits/stdc++.h>
using namespace std;
int main()
{
     cout << "Enter the number of data points: ";
    int n;
    cin>>n;
    double x[n],y[n];
    cout << "Enter the data points (x and y):"<<endl;
    for(int i=0;i<n;i++)
    {
        cout << "x[" << i << "] = ";
        cin>>x[i];
        cout << "y[" << i << "] = ";
        cin>>y[i]; 
    }
      // Create the Divided difference table
    double divDiff[n][n];
    for(int i=0;i<n;i++)
    {
        divDiff[i][0]=y[i];
    }
    for(int i=1;i<n;i++)
    {
        for(int j=0;j<n-i;j++)
        {
             divDiff[j][i] = (divDiff[j+1][i-1] - divDiff[j][i-1])/(x[i+j]-x[j]);
        }
    }
   
     cout << endl << "DIVIDED DIFFERENCE TABLE" << endl;
     for(int i =0;i<n;i++)
     {
        cout<<x[i];
        for(int j = 0; j<n-i;j++)
        {
            cout<<" \t "<<divDiff[i][j];
        }
        cout<<endl;
     }
     
     double value;
     cout << "Enter the value to interpolate: ";
     cin>>value;
     double result = y[0];
     double term = 1.0;
     for(int i=1;i<n;i++)
     {
          term *= (value - x[i-1]);
          result += term * divDiff[0][i];
      
     }
     cout << "Interpolated value at " << value << " is " << result <<endl;
    return 0;
}
