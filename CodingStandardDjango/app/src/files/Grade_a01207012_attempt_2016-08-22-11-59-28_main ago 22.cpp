#include <iostream>

using namespace std;

//define variable

double getGrade(string message)
{

//get dGrade value

  cout << message << endl;
  
  double dGrade;
  
  cin >> dGrade;

  return dGrade;

}

//define char variable

char GradeCalc(double dg)
{

  
  char cg;

 
 //defining letter for grade
 
  if(dg >= 90)
  {
    cg = 'A';
  }
  else if(dg >= 80)
  {
    cg = 'B';
  }
  else if(dg >= 70)
  {
    cg = 'C';
  }
  else if(dg >= 50)
  {
    cg = 'D';
  }
  else
  {
    cg = 'E';
  }

  return cg;
}

//display final message

void display(double dGrade, char cgrade){
  cout << "Your grade is " << dGrade << endl << "With the letter " << cgrade << endl;
}


int main () 
{
  
  //ask for value
  
  double dGrade = getGrade("Enter the grade: ");

  char cgrade = GradeCalc(dgrade);
  
  display(dGrade,cgrade);

  return 0;
}

