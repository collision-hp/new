//Visualize a situation where you want to change your upi pin but you donot want the original value to change in your atm pin.
//PASS BY VALUE copy of the value is passed to the function (that changes) while the actual value doesn't change
#include<iostream>
using namespace std;
int globalTea
void Cups(int cups){
    cups+=5;
    cout<<"Poured cups "<<cups<<endl;
}
int main(){
    int cups=5;
    Cups(cups);
    cout<<"Number of cups are "<<cups<<endl;
}

/*SCOPE OF A VARIABLE
Outside things(declared variables) can be accessed inside the function like int globaltea
But inside things(declared variables) inside a function cannot be accessed outside the function. like int cups=5*/


/*Imagine a situation where your upi pin and atm pin are the same ,you are changing your upi password through your mobile phone 
and you want to sync that change in your bank account atm card simultaneously */
//PASS BY REFERENCE reference of the value is passed to the function and the changes made inside the function affects the original value
#include<iostream>
using namespace std;
void Cups(int &cups){
    cups+=5;
    cout<<"Poured cups "<<cups<<endl;
}
int main(){
    int cups=5;
    Cups(cups);
    cout<<"Number of cups are "<<cups<<endl;
} 