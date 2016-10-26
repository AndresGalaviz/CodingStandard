/*
    Grade Program.cpp

    This aplication ask the user for a grade and
    then it give you back a character letter.

    Marlon Omar López Aguilar
    A01139431
    22/08/2016
    version 1.0
*/

#include <iostream>

#include <cmath>

using namespace std;
/*

    Function: Grade
        This function is use for get the grade from the user
        when a mesagge is display.
    Parameters:
        sMessage: this is a string that is use for insert the message
                  that you display to the user.
    Returns: You return the variable dGradde which is a value that the user
             gives you.

*/
double Grade(string sMessage)
{
    // this is the variable to store the grade
    double dGrade;
    // this is for display the mesagge to ask for grade
    cout << sMessage << endl;
    cin >> dGrade;
    return dGrade;

}
/*

    Function: Letter
        This function characther that calculates the letter tdepending
        on the grade the user inputs.
    Parameters:
        dGrade: is were the grade is store and it is use to calculate the
                the letter.

    Returns: it return de value cLetter that gives you the letter depending
             on the grade.

*/
char Letter (double dGrade)
{
    //this is the variable were we are gooing to store the letter
    char cLetter;
    //if are for doing the validations to difinding the letter
    if (dGrade < 50 )
    {
        cLetter = 'E';
    } else if(dGrade < 70 )
    {
        cLetter = 'D';
    } else if (dGrade < 80 )
    {
        cLetter = 'C';
    } else if (dGrade < 90 )
    {
        cLetter = 'B';
    } else if (dGrade <= 100 )
    {
        cLetter = 'A';
    }
    return cLetter;
}
/*

    Function: Message
        This function is a void that displays the messages to give the user
        the results of the program.
    Parameters:
        dGrade: is were the grade is store and it is use to display the grade
                the user input.
        cLetter: is were the letter is store and is use for diplaying the letter

    Returns: its a void so it has no returns

*/
void Message (double dGrade, char cLetter )
{
    //this is for diplaying the grade
    cout << "This is your grade: " << dGrade << endl;
    //this is for diplaying the letter
    cout << " You have a:  "<< cLetter << endl;
}
int main() {
    //here you are difinding a variable by calling the function Grade
    double dGrade = Grade("Enter Grade: ");
    //here you are difinding a variable by calling the function letter
    char cLetter = Letter(dGrade);
    //here you are difinding a variable by calling the function message to display the message
    Message (dGrade, cLetter);

    return 0;
}
