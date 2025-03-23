#include<iostream>
using namespace std;

int main(){
    int chai[3][6]={1,2,3,4,5,6,11,12,13,14,15,16,21,22,23,24,25,26};
    for(int i=0;i<3;i++){
        cout<<"I am at shop "<<i+1<<endl;
        for(int j=0;j<6;j++){
            cout<<chai[i][j]<<" ";
        }
        cout<<"\n";
    }
}