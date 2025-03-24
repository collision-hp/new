#include<iostream>
using namespace std;
int main(){
    int hour;
    cout<<"Enter the number of hours";
    cin>>hour;
    if (hour>8 && hour<18){
        cout<<"Shop is open";
    }
    else{
        cout<<"Shop is closed";
    }
    
    return 0;
}