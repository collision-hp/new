#include<iostream>
using namespace std;

int main(){
    int tea;
    cout<<"Enter the number of cups you want";
    cin>>tea;
    if (tea<10){
        tea+=5;
    }
    cout<<"The number of tea bags are"<<tea;
    return 0;

}