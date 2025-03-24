#include<iostream>
#include<vector>
using namespace std;

class Chai{
    public:
    //attributes
        string tname; //name of tea
        int servings;//number of tea
        vector<string> ingredients; //list of ingredients for tea

    //Member Function
        void display(){
            cout<<"Tea name "<<tname<<endl;
            cout<<"Servings "<<servings<<endl;
            cout<<"Ingerdients: "<<endl;
            for(string ingredient:ingredients){
                cout<<ingredient<<endl;
            }
        }
};
int main(){
    Chai c1;
    c1.tname="Lemon Tea";
    c1.servings=2;
    c1.ingredients={"Water","Lemon"};
    c1.display();

    Chai c2;
    c2.tname="Masala Tea";
    c2.servings=3;
    c2.ingredients={"Masala","Milk"};
    c2.display();
    return 0;
}