// Given an array of integers nums and an integer target, return indices of the two numbers 
//such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same 
//element twice.
// You can return the answer in any order.

#include <stdio.h>
int main(){
    int nums[5]={1,2,3,4,5};
    int target =3;
    int i,j;
    int result1, result2;
    for (i=0;i<5;i++){
        for (j=i+1;j<5;j++){
            if (nums[i]+nums[j]==target){
                result1=i;
                result2=j;
                printf("The indices are %d and %d. \n", result1, result2);
                printf("Enjoy Programming\n");
            }
        }
    } 
    return 0;
}
