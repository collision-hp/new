#include<iostream>
#include<string>
using namespace std;
int check_Temp(int temp){
    return temp;
}
void cups(int no){
    cout<<"Number of cups are "<<no<<endl;
}
int check_Temp(string chai){    // method-overloading
    cout<<"The temperature of Tea cup is "<<chai<<endl;
}
int main(){
    int temp=21;
    int no=3;
    string chai="found to be 20 degree celsius";
    cout<<check_Temp(temp)<<endl;
    cups(no);
    check_Temp(chai);
    return 0;
}
