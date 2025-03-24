#include<iostream>
#include<string>
using namespace std;
int main(){
    string str;
    int n=5;
    while (n<10){
        cout<<"Enter your choice";
        getline(cin,str);
        if(str=="green tea"){
            cout<<"Sorry";
            continue;
        }
        else{
            cout<<"Brewing";
        }
        n++;
    }
    
    return 0;
}