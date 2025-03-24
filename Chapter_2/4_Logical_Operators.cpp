#include<iostream>
using namespace std;
int main(){
    bool isStudent;
    int cups;
    cout<<"Are you a student \n 1 for True\n 0 for False";
    cin>>isStudent;
    cout<<"How many cups do you want";
    cin>>cups;
    if (isStudent || cups>15){
        cout<<"You are eligible for subscription discount";
    }
    else {
        cout<<"No you are not eligible";
    }
    return 0;
}