#include<iostream>
#include<string>
using namespace std;
int main(){
    string str;
    while (str!="no"){
        cout<<"Do you want tea??";
        getline(cin,str);
    }
    cout<<"Thank you";
    return 0;
}
