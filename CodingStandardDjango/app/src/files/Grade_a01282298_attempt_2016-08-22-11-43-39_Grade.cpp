#include <iostream>

using namespace std;

/*
    Grade.cpp

    This program assigns a letter to a grade depending on the value.
    
    Rafael Serna A01282298
    22 / Aug / 2016
    Version 1.0
*/

/*
    Grade

    Function to recieve the value of the grade.

    Parameters:
       sMessage     Sends the user a message to recieve the grade.
    Returns:
       dGrade       The value of the initial grade.
*/
double Grade(string sMessage)
{
  double dGrade;
  
  cout << sMessage;
  cin >> dGrade;
}

/*
    Letter

    Function to transform the numerical value to a specific letter.

    Parameters:
       dGrade       The numerical value of the grade.
    Returns:
       cLetter      The letter that will be asigned to the numerical grade.
*/
char Letter(double dGrade)
{
  char cLetter;
  
  if (dGrade < 50)
  {
    cLetter = 'E';
  }
  else if (dGrade < 70)
  {
    cLetter = 'D';
  }
  else if (dGrade < 80)
  {
    cLetter = 'C';
  }
  else if (dGrade < 90)
  {
    cLetter = 'B';
  }
  else if (dGrade <= 100)
  {
    cLetter = 'A';
  }

  return cLetter;
}

/*
    Message

    Displays the grade and letter of the user.

    Parameters:
       cLetter      Letter asigned to the grade.
       dGrade       Original grade of the user.
    Returns:
       None
*/
void Message(char cLetter, double dGrade)
{
    cout << "Your " << dGrade << " gets a " << cLetter << endl;
}

/*
    Main

    Asks for all the functions and sends the message for the user.

    Parameters:
      None
    Returns:
      An integer with value zero (no error result).
*/
int main()
{
  double dGrade = Grade("Enter the grade: ");
  char cLetter = Letter(dGrade);
  Message(cLetter, dGrade);
  
  return 0;
}