# include <iostream>
using namespace std;
int main(){
    
  float a , b;
  int option;
  cout<< "Enter a and b: ";
  cin>>a;
  cin>>b;
  int sum=a+b;
  int diff=a-b;
  float quotient=a/b;
  int product=a*b;

  cout<<"-----------------------Enter any option:------------------- "<<endl;
  cout<<"1. Sum"<<endl;
  cout<< "2. Difference"<<endl;
  cout<< "3. Product"<<endl;
  cout<<"4. Quotient"<<endl;
  cin>>option;
  switch (option){
    case 1:
         cout<<"Sum of "<<a <<" and " <<b<<" is: "<<sum<<endl;
         break;
    case2:
        cout<<"Difference of "<<a <<" and "<<b <<" is: "<<diff<<endl;
        break;
    
    case3:
        cout<<"Product of "<<a <<" and "<<b <<" is: "<<product<<endl;
        break;
    
    case 4:
        cout <<"Quotient of " <<a <<" and "<<b<<" is: "<<quotient<<endl;
        break;

    case5:
        cout<<"Invalid operators!!!"<<endl;
        exit(0);
    }
    return 0;

}

//type casting
