#include <iostream>

using namespace std;

/* 
    Main.cpp
    This program calculates the letter grade
    for the number grade imputed from the student.
    Jorge Andres Sabella 
    A01282292
*/
/* 
getGrade 
This function askes the user(student) for the grade.
Parameters:
The string message from the main.
return: The grade "dGrade"
*/

double getGrade(string messege)
{
    
    //declare Grade variable
    double dGrade;
    
    // user imput the Grade
    cout << messege << endl;
    cin >> dGrade;
    
    // returning the grade variable
    return dGrade;
    }
    
    /*
    calculatedChar
    This function calculates the letter number using the grade imputaded by the user.
    Parameters: double dGrade(the grade from gotten in function getGrade)
    Return: calgrade 
    */
char calculatedChar(double dGrade){
    
    //define calulated grade variable
    char calgrade;
    
    //if to get A, 90>
    if (dGrade >= 90 ){
        calgrade = 'A';
    }
    // else if to get B 90-80
        else if (dGrade >= 80 && dGrade < 90){    
        calgrade = 'B';
    }
    //else if to get B 80-70
        else if (dGrade >= 70 && dGrade < 80){
        calgrade = 'C';
    }       
    //else if to get B 70-50
        else if (dGrade >= 50 && dGrade < 70){
        calgrade = 'D';
    }
    //else if anything else is imputed
        else {
        calgrade = 'E';
    }
    
    // return that returnes the letter variable calgrade
    return calgrade;
}
    /*
    Display
    This function displayes the last message to the user.
    Parameters: double dGrade(the grade from gotten in function getGrade, char calgrade(the letter gotten in the function calculated char)
    Return: no return
    */
void Display(double dG, char cG)
// the final message displayed to the user  using the two variables declared gotten in other functions and declares in the ()
{
    cout << "Your calculated result is " << dG << " therefore your calcuted result is " << cG << endl;
}
    /*
    Main:
    This function calls all other functions to work. 
    Parameters: double dGrade(none)
    Return: to 0 for no errors 
    */
int main()
{
   cout << "Hello World" << endl; 
   // declare variable for the funcion to work with the others, string message
   double dgrade = getGrade("Please enter your grade");
   
   // declare variable for the funcion to work with the others
   char cgrade = calculatedChar(dgrade);
   
   // calls the other two variables from the function to work and display
   Display(dgrade,cgrade);
   
   return 0;
}

