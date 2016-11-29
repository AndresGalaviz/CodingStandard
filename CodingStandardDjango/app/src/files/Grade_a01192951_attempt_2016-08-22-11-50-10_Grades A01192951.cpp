#include <iostream>

using namespace std;

/*
    The program calcules the letter grade given its numeric value
    Fermin Maisterrena Viades    A01192951
    08/22/2016
    Version 1.0
*/

/*
GetGrade
To get the letter grade value, the user must insert the numeric value

Parameters:
dGrade
cGrade

Returns:
GetGrade
*/

double GetGrade(string sMessage)
{
    double dGrade;
    
    //Get value
    cout <<sMessage <<endl;
    cin >> dGrade;
    
    return dGrade;
}




//Calculate letter grade
char CalculateValue (double dGrade)
{
    // Define variable
    
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
    else if (dGrade >= 60 && dGrade < 70)
    { 
        cGrade = 'D';
    }
    else 
    { 
        cGrade = 'E';
    }
    return cGrade;
}

//Void function to display results

void Display (double dGrade, char cGrade)
{
    cout << "Your grade is:" << dGrade;
    cout << "It is equal to:" << cGrade;
}


/*
//MAIN FUNCTION//
Prompts grade values to calculate the letter grade
Parameters:
none
Ruturns:
value 0 (void function)
*/

int main()

{
    
    //Get Grade
    double dGrade = GetGrade("Enter Grade");
    // display the Letter
    char cValue = CalculateValue(dGrade);
    // Display final message
    Display (dGrade,cValue);
    

    return 0;

}





