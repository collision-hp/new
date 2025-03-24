#include<iostream>
using namespace std;
int main(){
    int cups;
    cout<<"Enter the number of cups";
    cin>>cups;
    int price=10;
    int total=cups*price;
    if(cups>=20){
        cout<<"20% discount";
        total-=total*20/100;
        cout<<total;
    }
    else if(cups>10 && cups<20){
        cout<<"10% discount";
        total-=total*10/100;
        cout<<total;
    }
    else if(cups<10){
        cout<<"No Discount !! Your total price is ";
        cout<<total;
    }
}