#include<iostream>
using namespace std;

int main(){
    int cups;
    double price ,total=0;
    cout<<"Enter the numbers of cups you want ";
    cin>>cups;
    cout<<"Enter your budget ";
    cin>>price;
    total=cups*price;
    
    if(total>100){
        //5% discount
        total-=total*0.05;
    }
    cout<<"The total price is "<<total;

    return 0;

}
