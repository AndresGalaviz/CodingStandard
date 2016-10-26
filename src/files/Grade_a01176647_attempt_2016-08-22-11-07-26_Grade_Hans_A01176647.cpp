/*
 Grade_Hans_A01176647.cpp

 This application calculates the letter 
 grade of a given number.
 Hans Nudding
 A01176647
 22 / Ag / 2016
*/
#include <iostream>
#include <math.h>

using namespace std;

/*
 GetGrade
 Gets a grade number from the user 
 Parameters:
 sDisp Message to display
 Returns:
 dGrade Grade number given by user
*/
double GetGrade(string sDisp)
{
    //Storing Variable
    double dGrade;
    //Getting value from user
    cout << sDisp << endl;
    cin >> dGrade;
    //Return variable
    return dGrade;
}
/*
 CalculateGrade
 Calculates the grade letter
 with a given number
 Parameters:
 dGrade Grade of user
 Returns:
 cLetGrade Letter grade
*/
char CalculateGrade(double dGrade)
{
    //Storing variable
    char cLetGrade;
    
    //Determine the Letter Grade
    if (dGrade >= 90)
    {
        cLetGrade = 'A';
    }
    else if (dGrade >= 80 && dGrade < 90)
    {
        cLetGrade = 'B';
    }
    else if (dGrade >= 70 && dGrade < 80)
    {
        cLetGrade = 'C';
    }
    else if (dGrade >= 50 && dGrade < 70)
    {
        cLetGrade = 'D';
    }
    else
    {
        cLetGrade = 'E';
    }
    
    //Return the LetterGrade variable
    return cLetGrade;
}

/*
 Display
 Displays the letter grade 
 and the number grade
 Parameters:
 cLetGrade Letter Grade
 dGrade Numerical Grade
 Returns:
 None
*/
void Display(char cLetGrade, double dGrade)
{
    //Display the grade letter
    cout << "Letter Grade = " << cLetGrade << endl;
    //Display the number grade
    cout << "Number Grade = " << dGrade << endl;
}

/*
 main
 Gets grade from user. Controls functions.
 Parameters:
 none
 Returns:
 none
*/
int main()
{
  //Storing variables
  double dGrade;
  char cLetGrade;
  
  //Asking values from user
  dGrade = GetGrade("Enter grade: ");
  
  //Getting LetterGrade with "CalculateGrade" function
  cLetGrade = CalculateGrade(dGrade);
  
  //Display grades with "Display" function
  Display(cLetGrade, dGrade);
  
  //End
   return 0;
}


