// Given an array of integers nums and an integer target, return indices of the two numbers 
//such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same 
//element twice.
// You can return the answer in any order.

#include <iostream>
using namespace std;

int main(){
    int num[5]={1,2,3,4,5};
    int target=3;
    for (int i=0;i<5;i++){
        for(int j=i+1; j<5; j++){
            if (num[i]+num[j]==target){
                int result1=i;
                int result2=j;
                cout<<"The indices are: "<<result1<<" and "<<result2<<endl;
            }
        }
    }
    return 0;
}
