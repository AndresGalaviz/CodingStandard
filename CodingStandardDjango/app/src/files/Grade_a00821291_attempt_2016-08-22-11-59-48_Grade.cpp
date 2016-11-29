#include <iostream>
#include <math.h>
using namespace std;
double Getgrade(string sGreat)
{ double dGrade;
    cout << sGreat;
    cin >> dGrade;
return dGrade;
}    
char CalculateGrade(double dGrade)
{
    char cGrade;
    if (dGrade >= 90 && dGrade <= 100)
    {
        cGrade = 'A';
    }
    else if (dGrade >= 80 && dGrade <90)
    {
        cGrade = 'B';
    }
    else if (dGrade >= 70 && dGrade <80)
    {
        cGrade = 'C';
    }
    else if (dGrade >= 50 && dGrade <70)
    {
        cGrade = 'D';
    }
    else if (dGrade <50 && dGrade>=0)
    {
        cGrade = 'E';
    }
return cGrade;
}
void Display (double dGrade, char cGrade)
{
    cout << "Your grade is" << dGrade << "And your rank is " << cGrade << endl;
}
int main()
{
    double dGrade = Getgrade("Get grade");
    char cGrade= CalculateGrade(dGrade);
    
    
    Display(dGrade, cGrade);
 
   
   return 0;
}

