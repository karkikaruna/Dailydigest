// Given an array arr[] of non-negative integers, where each element
//  arr[i] represents the height of the vertical lines, find the maximum amount 
//  of water that can be contained between any two lines,
//  together with the x-axis.

#include <iostream>
using namespace std;

void maxwater(int arr[], int n){
    
    int max=arr[0]+ arr[1];
    for (int i=0; i<n; i++){
        for (int j=i+1; j<n ; j++){
            if (arr[i]+arr[j]>max){
                max=arr[i]+arr[j];
                cout<<"maximum height is"<<max<<endl;
            }
    }
        
    }
}

int main(){
    int arr[]={1,2,3,4,5};
    int n=sizeof(arr);
    maxwater(arr, n);
    return 0;
}