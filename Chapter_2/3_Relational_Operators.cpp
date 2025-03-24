#include<iostream>
using namespace std;

int main(){
    int cups;
    cout<<"Enter the number of cups you want";
    cin>>cups;
    if(cups>20){
        cout<<"You got a Golden Badge";
    }
    else if (cups>=10 && cups<=20){
        cout<<"You got a Bilver Badge";
    }
    else{
        cout<<"ALAS no badge";
    }
    return 0;
}