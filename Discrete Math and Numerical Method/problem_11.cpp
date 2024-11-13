#include <bits/stdc++.h>
using namespace std;
int main()
{
    double a, b, c;
    cout << "Enter the coefficents of the equation(ax^2+bx+c) :";
    cin >> a >> b >> c;
    double ub, lb;
    cout << "Enter the lower bound of the interval:";
    cin >> lb;
    cout << "Enter the upper bound of the interval:";
    cin >> ub;
    double fa = a * lb * lb + b * lb + c;
    double fb = a * ub * ub + b * ub + c;

    if(fa * fb >=0)
    {
        return 0;
    }

    double Ep = 0.0001;
    double root;
  
    while ((ub - lb) >= Ep)
    {
        root = ub - ((fb * (ub - lb)) / (fb- fa));
        double fc = a * root * root + b * root + c;
        if (fc == 0.0)
        {
            cout<<"Root = "<<root<<endl;
            return 0;
        }
       else if (fa * fc < 0)
        {
            ub = root;
            fb = fc;
        }
        else
        {
            lb = root;
            fa = fc;
        }
    }
    
    cout << "Root = " << root << endl;
    return 0;
}
