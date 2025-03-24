#include<iostream>
using namespace std;
int main(){
    //lambda->function without name ,when the function is only used one ,for efficient memory management
    auto tea=[](int cups,int quan){
        cout<<"Preparing "<<cups<<" of tea with "<<quan<<" kg of sugar"<<endl;
    };

    tea(4,10);
    return 0;
}