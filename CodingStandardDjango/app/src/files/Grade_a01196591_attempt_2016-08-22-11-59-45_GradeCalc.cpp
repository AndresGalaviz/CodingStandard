#include <iostream>

using namespace std;

double GetGrade(string sMessage)
{      
      cout << sMessage << endl;
      cin >> GetGrade;
      
      return GetGrade
}

char Display(double vGrade)
{
    if (vGrade >=90) {
        cout << "You got an A" << endl;
    }       
    
    else if (vGrade >=80 <90){
        cout << "You got a B" << endl;
    }
    
    else if (vGrade >=70 <80){
        cout << "You got a C" << endl;
    }
    
    else if (vGrade >= 50 <70){
        cout << "You got a D" << endl;
    }
    
    else if (vGrade < 50){
        cout << "You got an E" << endl;
    }
    
}

int main()
{
    // get grade
    double dGrade = GetGrade("Enter Grade");
    
    cout <<  Display(dGrade);
 
   return 0;
}

