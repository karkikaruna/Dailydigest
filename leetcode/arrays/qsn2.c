// Given two sorted arrays nums1 and nums2 of size m and n respectively, 
// return the median of the two sorted arrays.
// The overall run time complexity should be O(log (m+n)).
#include <stdio.h>
#include <stdlib.h>
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
  float median=0;
  int i;
  for (i=0;i<=nums1Size;i++){
    median=median+i;
  } 
  return median; 
}

int main(){
    int nums1[]={1,2,3,4,5}, nums2[]={2,3,4,5,6}, m,n,nums1Size=5, nums2Size=5;
    findMedianSortedArrays(nums1, 5, nums2, 5);
    return 0;
}