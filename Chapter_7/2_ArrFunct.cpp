#include<iostream>
using namespace std;
int total(int n){
    int chaino[n];
    int total=0;
    for(int i=0;i<n;i++){
        cout<<"Enter your no. of chai for your friend "<<i<<endl;
        cin>>chaino[i];
        total+=chaino[i];
    }
    return total;
}

int main(){
    int x=total(5);
    cout<<x;
    return 0;

}