//Paulina De La Garza
//A01193671
#include <iostream>
#include <math.h>

using namespace std;

double GetGrade(string sMessage)
{
    double dGrade;
    
    cout<< sMessage <<endl;
    cin<< dGrade;
    
    return dGrade;
}

char CalculateGrade(double dGrade)
{
    char cGrade;
    
    if (dGrade >=90 )
    {
    cGrade = 'A';
    }
    
    else if (dGrade >=80 && dGrade <90 )
    {
    cGrade= 'B';
    }
    
    else if (dGrade >=70 && dGrade <80 )
    {
    cGrade= 'C';
    }
    
    else if (dGrade >=70 && dGrade <50 )
    {
    cGrade= 'D';
    }
    
    else (dGrade < 50)
    {
    cGrade= 'E';
    }
    
    return cGrade; 
}

void Display (dGrade, cGarde);

{
    cout<< "your grade is" << dGrade << "that is equal to" << cGrade << endl;
}

int main()
{
    double dGrade;
    
    
    dGrade = GetGrade("your grade is");
    
    char cGrade = CalculateGrade(dGrade);
    
    Display(dGrade, cGrade);
    
    return 0;
    
}