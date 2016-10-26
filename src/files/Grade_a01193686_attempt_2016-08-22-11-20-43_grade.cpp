#include <iostream>
#include <math.h>

using namespace std;

double GetGrade (string sMessage)
{
    double dGrade;
    
   //Get value from the user
   cout << sMessage << endl;
   cin >> dGrade;
   
    return dGrade;
}

char CalculateLetter (double dGrade)
{
    char cValue;
    
    if (dGrade >= 90){
       cValue = 'A';
    }
    
    else if (dGrade >= 80 && dGrade < 90){
        cValue = 'B';
    }
    
    else if (dGrade >= 70 && dGrade < 80){
        cValue = 'C';
    }
    
    else if (dGrade >= 50 && dGrade < 70)
    {
        cValue = 'D';
    }
    
    else 
    {
        cValue = 'E';
    }
    
        return cValue;
    
}

void Display (double dGrade, char cValue)
{
    cout << "Your grade is " << dGrade << ", which is equal to " << cValue << endl;
}

int main()
{
    // Get grade from the user
   double dGrade = GetGrade ("Enter grade"); 
   
   // Get value
   char cValue = CalculateLetter (dGrade);
   
   // Display results
   Display (dGrade, cValue);
   
   return 0;
}


