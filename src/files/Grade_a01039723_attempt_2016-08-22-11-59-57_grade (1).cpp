/*Jose David Arreola Mendez
A01039723
Programming Fundamentals
Grade Application
*/

/*This app will help you change the value of a grade from numerical to letters
#include <iostream>
using namespace std;


/*This function will ask for the grade 
    Parameters:
        FirstGrade: Gives you the first grade in numbers
    Returns:
        Saves the grade
        */
double firstGrade (string sMessage)
{
    //define the variable
    double dGrade;

    //Get the value from the user
    cout << sMessage << endl;
    cin >> dGrade;
    return dGrade;
}

/*This function will calculate the letter
    Parameters:
        SecondGrade: Gives you the grade in Letters
    Returns:
        Saves the grade in letter
        */
char secondGrade(double dFirstGrade)
{
    char cCheckLetter;
    
    if (dFirstGrade >=90)
    {
        cCheckLetter = 'A';
    }
    else if (dFirstGrade >= 80 && dFirstGrade < 90 )
    {
        cCheckLetter = 'B';
    }
    else if (dFirstGrade >=70 && dFirstGrade <80)
    {
        cCheckLetter = 'C';
    }
    else if (dFirstGrade >=50 && dFirstGrade < 70)
    {
        cCheckLetter = 'D';
    }
    else if(dFirstGrade >=0 && dFirstGrade <50)
    {
        cCheckLetter = 'E';
    }
    return cCheckLetter;
}
    

/*This function will show the grade and the character
    Parameters:
        FirstGrade: Gives the grade in numerical value
        SecondGrade: Gives the grade in letters
        DisplayGrade: Displays the grade in letter
    Returns:
        The grade in letters.
        */
        
string displayGrade(double dFirstGrade, char cCheckLetter)
{
    cout << "Your grade is: " << endl;
}

int main()
{
    //define the variables needed
    double dFirstGrade = dGrade("Enter your grade: ");
    char cSecondGrade;
    double dGetGrade;
    
    //Introduce the app
    cout << "Hello. This app will help you to check what grade you get in chacters" << endl;
   
   //Gives the numerical value a letter value
    char cGrade = getGrade(dFirstGrade);
    
    //Displays the letter
    displayGrade (dFirstGrade, cCheckLetter);
    return 0;
}