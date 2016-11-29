#include <iostream>

using namespace std;

/*
    main.cpp

    This program calculates a letter
    grade correpsonding to the inputed
    number grade inputed by the user

    Eduardo Aguilar leal    A01193626
    11/22/2016
    Version 1.0
*/

/*
    getGrade

    It prompts the user for
    the number grade

    Parameters:
        messege   it is the string messege displayed to the user

    Return: the inputed grade  dgrade
*/
double getGrade(string messege){

  //display messege
  cout << messege << endl;
  //declare variable
  double dgrade;
  //save value in variable
  cin >> dgrade;

  return dgrade;

}

/*
    calcaulateGrade

    It calcualtes the the user's
    letter grade depneding on the
    inputed number grade

    Parameters:
        dg  the number grade

    Return: the determined letter grade
*/
char calcualateGrade(double dg){

  //declare messege
  char cg;

  //ifs that determine letter grade
  if(dg >= 90){
    cg = 'A';
  }
  else if(dg >= 80){
    cg = 'B';
  }
  else if(dg >= 70){
    cg = 'C';
  }
  else if(dg >= 50){
    cg = 'D';
  }
  else{
    cg = 'E';
  }

  return cg;
}
/*
    display

    Dsiplays the user's
    grades

    Parameters:
        dgrade  the number grade inputed by the user
        cgrade  the letter grade corrsponding the number grade

    Return: none, void function
*/
void display(double dgrade, char cgrade){
  cout << "Your inputed grade is " << dgrade << endl << "therfore your calcualted result is " << cgrade << endl;
}

/*
    main

    It calls all other functions
    in an spcecic order for the purpose of the
    program working

    Parameters:
        none

    Return: 0 for the sake of no errors
*/
int main () {
  //decalre variable for number grade
  double dgrade = getGrade("Please insert your grade");
  //decalre varibale for charcater grade
  char cgrade = calcualateGrade(dgrade);
  //call function for displaying results
  display(dgrade,cgrade);

  return 0;
}
