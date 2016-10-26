/*
 Grade.cpp
 
 This program gets a numerical grade from the user and 
 displays the corresponding character for it.

 Omar Iván Flores Quijada
 22/08/2016
 Version 1.0
*/

#include <iostream>
using namespace std;

/*
 	getGrade

 	Uses a string to ask the user to enter a numerical
	grade and then it returns that value.

 	Parameters:
 	sFrase message for the user
 	Returns:
 	returns the value that the user entered.
*/

double getGrade(char sFrase[20])
{
	double dGrade;
	cout << sFrase << ": ";
	cin >> dGrade;
	return dGrade;
}

/*
 	calculateGrade

 	It looks for the corresponding character for
 	the entered grade. 

 	Parameters:
 	dGrade numerical grade
 	Returns:
 	cGrade character grade
*/

char calculateGrade(double dGrade)
{
	char cGrade;
	if(dGrade>=90)
	{
		cGrade = 'A';
	}
	else if(dGrade>=80)
	{
		cGrade = 'B';
	}
	else if(dGrade>=70)
	{
		cGrade = 'C';
	}
	else if(dGrade>=50)
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
 	toDisplay

 	Displays the numerical grade and a character in a message

 	Parameters:
 	dGrade numerical grade
 	cGrade character grade
 	
 	returns:
 	none
*/

void toDisplay(double dGrade, char cGrade)
{
	cout << "Your grade is " << cGrade << " (" << dGrade << ")";
}

/*
 Main Function

 Prompt values for mass and acceleration to calculate the
 force for a moving object, using the function caclulateForce
 and display the result.

 Parameters:
 none
 Returns:
 an integer value with the error number (0 = none)
*/

int main()
{
	// display a message and get a double value
	double dGrade = getGrade("Enter the grade");
	// display the double value and a character value
	toDisplay(dGrade,calculateGrade(dGrade));
	// return 0
	return 0;
}
