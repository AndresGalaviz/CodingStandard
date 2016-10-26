#include <iostream>
using namespace std;

double GetGrade(string sMessage)
{
    double dGrade;
    
    cout << sMessage << endl;
    cin >> dGrade;
    
    return dGrade;
}

char CalculateGrade(double dGrade)
{
    char cGrade:
    if (dGrade >=90)
    {
       cGrade= 'A';
    }
    else if (dGrade>= 80 && dGrade < 90)
    {
        cGrade= 'B';
    }
    else if (dGrade>= 70 && dGrade < 80)
    {
        cGrade= 'C';
    }
    else if (dGrade>= 50 && dGrade < 70)
    {
        cGrade= 'D';
    }
    else
    {
        cGrade= 'E';
    }
    return cGrade;
}

void display (double dGrade, char cGrade)
{
    cout<<  calculateGrade(double dGrade) << endl;
    cin>>
      
}


int main()
{
// get the grade from the user
double dGrade =  getGrade("input your grade")

char cGrade = CalculateGrade(dGrade)

//display the letter

Display (dGrade, cGrade);
cout <<"character= " << calculateGrade(double dGrade)<<endl;
   
   return 0;
}

