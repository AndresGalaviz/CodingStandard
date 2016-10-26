#include <iostream>
#include <math.h>

using namespace std;
/*
 Grade.cpp

 This application calculates the grade and displays the character based on the 
 given criteria.
 
 Maria Andrea Garcia
 22 / August / 2016
 version 1.0
*/

double GetGrade(string sMessage)
{
    double dGrade;
    
    cout << sMessage << endl;
    cin >> dGrade;
    
    return dGrade;
    
}
    
char GetLetter(double dGrade)
{   
    char cGrade;
    
     if (dGrade >= 90)
     { 
         cGrade = 'A';
     }
     else if (dGrade >= 80 && dGrade < 90)
     {
         cGrade = 'B' ;
     }
     else if (dGrade >= 70 && dGrade < 80)
     {
         cGrade = 'C';
     }
     else if (dGrade >= 50 && dGrade < 70)
     {
         cGrade = 'D';
     }
     else 
     { 
         dGrade = 'E' ;
     }
     return cGrade;
}

void Display (double dGrade, char cGrade)
{
    cout << "Your grade is:" << dGrade;
    cout << "It is equal to:" << cGrade;
}


    /*
 dGrade
 Calculates the grade given the number by the user.
 Parameters:
 
 Grade                    Character

>=90                         A

>=80   <90                   B

>= 70  <80                   C

>= 50  < 70                  D

anyother                     E

 Returns:
 cGrade in a character.
*/
int main()
{
 
     // get grade
    double dGrade  =  GetGrade("Enter Grade:");
    
    // calculate letter
    char cGrade = GetLetter(dGrade);
    
    // display the letter
    Display (dGrade, cGrade);
   
   return 0;
}

