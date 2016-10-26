/*
   GradeCharacter.cpp
   
   This application gets displays a character depending on 
   the grade given by the user
   
   Sergio Canto
   22 / August / 2016
   version 1.0
*/

#include <iostream>

using namespace std;

/*
   GetGrade
   
   Gets the grade from the user
   Parameters:
      sGrade   message to get grade
   Returns:
      dGrade   grade from the user
*/  

double GetGrade(string sGrade)
{
    double dGrade;
    
    cout << sGrade << endl;
    cin >> dGrade;
    
    return dGrade;
}

/*
   CalculateGrade
   
   Conditions a letter depending on the grade
   Parameters:
      dGrade   grade given by the user
   Returns:
      cGrade   letter
*/  

char CalculateGrade(double dGrade)
{
    char cGrade;
    
    if (dGrade >= 90)
    {
        cGrade = 'A';
    }
    
    else if (dGrade >= 80 && dGrade < 90)
    {
        cGrade = 'B';
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
        cGrade = 'E';
    }
    
    return cGrade;
}

/*
   Display
   
   Displays a message with the grade and the letter
   Parameters:
      dGrade   grade given by the user
      cGrade   letter
   Returns:
      None
*/  

void Display(double dGrade,char cGrade)
{
    cout << "Your grade is " << dGrade << " and your character is " << cGrade << endl;
}

/*
   Main Function

   Prompt gets a grade from the user, get a letter depending
   on the grade and displays a message with both values

   Parameters:
      None
   Returns:
      an integer value with the error number (0 = none)
*/

int main()
{
    //Get grade
    double dGrade = GetGrade("Enter Grade");
    
    //Calculat letter
    char cGrade = CalculateGrade(dGrade);
    
    //Display the message with the grade and the letter
    Display (dGrade,cGrade);
   
   return 0;
}