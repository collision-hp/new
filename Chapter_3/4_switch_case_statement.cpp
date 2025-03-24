#include<iostream>
using namespace std;
int main(){
    int choice;
    cout<<"1-Green Tea\n2-Black Tea\n3-Masala Tea";
    cin>>choice;
    switch (choice){
    case 1:
        cout<<"Price - 10$";
        break;
    case 2:
        cout<<"Price - 20$";
        break;
    case 3:
        cout<<"Price - 30$";
        break;
    default:
        cout<<"Unavailable";
        break;
    }
}