//David Fernandez Guzman
//A01193529
//Claswork Grades

#include <iostream>

using namespace std;

double GetGrade(string message)
{
    //To store number grade form user
    double dGrade;
    //To get number grade from user
    cout<< message<< endl;
    cin>> dGrade;
    //send number grade to main
    return dGrade;
}

char CalculateGrade(double dGrade)
{
    //To store character grade
    char cGrade;
    //To get character grade depending on number grade and conditions
    if(dGrade >= 90)
    {
        cGrade = 'A';
    }
    else if(dGrade >= 80 && dGrade < 90)
    {
        cGrade = 'B';
    }
    else if(dGrade >= 70 && dGrade < 80)
    {
        cGrade = 'C';
    }
    else if(dGrade >= 50 && dGrade < 70)
    {
        cGrade = 'D';
    }
    else
    {
        cGrade = 'E';
    }
    return cGrade;
}

void Display(double dGrade, char cGrade)
{
    //To display number grade and character grade
  cout << "Your number grade is " << dGrade << endl << "and your calcualted grade is " << cGrade << endl;
}

int main()
{
    
   // get grade
    double dGrade  =  GetGrade("Enter Grade");
    // calculate letter
    char cGrade = CalculateGrade(dGrade);
    // display the letter
    Display(dGrade,cGrade);
   
   return 0;
}

