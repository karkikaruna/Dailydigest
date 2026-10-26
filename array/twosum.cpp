// Given an array arr[] of n integers and a target value, check if there exists a 
// pair whose sum equals the target.
# include <iostream>
using namespace std;

bool twosum(int arr[], int target, int n){
   
    for (int i=0; i<n; i++){
        for (int j=i+1; j<n; i++){
            if (arr[i]+ arr[j]==target ){
                return true;
            }
        }
    } 
    return false;
      
}
int main(){
    int arr[]={1,2,3,5,6};
    int n=sizeof(arr);
    int target=3;
    if (twosum(arr, target, n)){
        cout<<"Target Found!"<<endl;

    }
    else cout<<"Target not Found!"<<endl;
    return 0;


}