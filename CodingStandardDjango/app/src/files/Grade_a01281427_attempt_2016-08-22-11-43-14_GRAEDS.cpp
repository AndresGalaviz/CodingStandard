/* Grading system
    with the program you will enter your numerica grade of a certai course and it will
    calculate the alphabetical grade from that
    
    Genki Matsumura
    a01281427
    22/08/2016
    version 1.0
    
*/

#include <iostream>

using namespace std;

/* getting grade
this gunction is used to display a message and to get the grade from the user
parameters : sDisp
returns: value obtained from user
*/

//getting the grade
    
double Grade (string sDisp)
    {
        double dGrade;
        cout << sDisp<< endl;
        cin >> dGrade;
        return dGrade;
        
    }

/* letter grade
here the function uses the numeric grade entered to calculate the alphabetical grade
parameters: dGrade
returns: alphabetical grade
*/

//calculate letter

char letGrade (double dGrade)
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
        else if (dGrade < 50 && dGrade > 0)
        {
            cGrade = 'E';
        }
    return cGrade;
}
        
/* Dkisplaying
in this function we display simply both grades
para,eters: cGrade and dGrade
returns: none
*/
void Display (double dGrade, char cGrade)
    {
        
        cout << "your numeric grade is : "<< dGrade << endl;
        cout << "your alphabetic grade is : " << cGrade << endl;
        
    }
    
/* call functions to use in the main to simplify the use of the main
*/
int main()
{
   double dGrade;
   char cGrade;
   
   dGrade = Grade(" Enter the Grade : ");
   cGrade = letGrade(dGrade);
   Display (dGrade, cGrade);
   
   return 0;
}

