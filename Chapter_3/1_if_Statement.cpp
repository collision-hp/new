//write a program thats check whether the user want to order Green tea. if the user types "Green Tea" the program should confirm their order

#include<iostream>
#include<string>
using namespace std;
int main(){
    string tea;
    cout<<"Enter the type of tea you want ";
    getline(cin,tea);
    if(tea == "Green Tea"){
        cout<<"You have ordered Green Tea";
    }
    return 0;
}