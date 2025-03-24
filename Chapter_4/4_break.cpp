#include<iostream>
#include<string>
using namespace std;
int main(){
    string str;
    while(true){
        cout<<"Start or Continue or Stop";
        getline(cin,str);
        if(str=="Stop"){
            break;
        }
        else{
            continue;
        }
    }
    return 0;
}