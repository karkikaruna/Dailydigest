# include <iostream>
using namespace std;

int main(){
    int marks[5]={1,4,56,0,7};

    int size=5;
    int smallest=marks[0];
    int largest=marks[0];
    int i;
    for (int i=1; i<5; i++){
        if (marks[i]<smallest){
            smallest=marks[i];
            
        } 
        
    }
    cout<<"smallest number is "<<marks[i]<<"and index is "<<i<<endl;
    

    for (int i=1; i<5; i++){
        if (marks[i]>largest){
            largest=marks[i];
        }
        
        
    }
    cout<<"largest number is"<<marks[i]<<"and index is"<<i<<endl;
    
  
}
