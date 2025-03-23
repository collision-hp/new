#include<iostream>
using namespace std;
int *notea(int cups){
    int *order= new int[cups];
    for (int i=0;i<cups;i++){
        order[i]=(i+1)*10; // since 1st is 0 ,so now it will continueas 10 20 30...
    }
    return order;
}
int main(){
    int cups=6;
    int* chaiorder=notea(cups);
    for(int i=0;i<cups;i++){
        cout<<"Cups "<<i+1<<"has "<<chaiorder[i]<<" mls\n";
    }
    delete[] chaiorder;
    return 0;
}