#include <iostream>

using namespace std;

double GetGrade(string sMessage)
{
    double dGrade;
    cout << sMessage;
    cin >> dGrade;
    
    return dGrade;
}

char Calculate(double dGrade)
{
    char cGrade;
    if(dGrade >= 90)
    {
        cGrade = 'A';
    }
    else if(dGrade >= 80)
    {
        cGrade = 'B';
    }
    else if(dGrade >= 70)
    {
        cGrade = 'C';
    }
    else if(dGrade >= 50)
    {
        cGrade = 'D';
    }
    else
    {
        cGrade = 'E';
    }
    return cGrade;
}


void Display(char cGrade)
{
    cout << "The Grade is: "<< cGrade;
}


int main()
{
    double dGrade = GetGrade("Enter Grade: ");
   
   return 0;
}

