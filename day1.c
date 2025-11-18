// Given an array arr[] of n integers and a target value, 
// check if there exists a pair whose sum equals the target. 
// This is a variation of the 2-Sum problem.

//method 1 naive approach
//Time complexity : O(n^2) 
//Space complexity: O(1)

#include <stdbool.h>
#include <stdio.h>

bool twoSum(int arr[], int n, int target){

    for (int i = 0; i < n; i++){

        for (int j = i + 1; j < n; j++){

            if (arr[i] + arr[j] == target)
                return true;
        }
    }
    return false;
}
int main(){

    int arr[] = {0, -1, 2, -3, 1};
    int target = -2;
    int n = sizeof(arr) / sizeof(arr[0]);

    if (twoSum(arr, n, target))
        printf("true\n");
    else
        printf("false\n");
  
    return 0;
}



//Method 2 Time: O(nlog(n)) 
//space: O(1)
//sorting and binary search approach
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>


int compare(const void *a, const void *b){
    return (*(int *)a - *(int *)b);
}

bool binarySearch(int arr[], int left, int right, int target){
    while (left <= right){
        int mid = left + (right - left) / 2;

        if (arr[mid] == target)
            return true;
        if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return false;
}

bool twoSum(int arr[], int n, int target){
 
    qsort(arr, n, sizeof(int), compare);

    for (int i = 0; i < n; i++){
        int complement = target - arr[i];

        if (binarySearch(arr, i + 1, n - 1, complement))
            return true;
    }
    return false;
}

int main(){
    int arr[] = {0, -1, 2, -3, 1};
    int target = -2;
    int n = sizeof(arr) / sizeof(arr[0]); 

    if (twoSum(arr, n, target))
        printf("true\n");
    else
        printf("false\n");

    return 0;
}


//method 3 Sorting and Two pointer Technique 
//Time : O (nlog(n)) Space : O(1)

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

// Comparison function for qsort
int compare(const void *a, const void *b){
    return (*(int *)a - *(int *)b);
}

bool twoSum(int arr[], int n, int target){
    
    qsort(arr, n, sizeof(int), compare);

    int left = 0, right = n - 1;

    while (left < right){
        int sum = arr[left] + arr[right];

        if (sum == target)
            return true;
        else if (sum < target)

            left++; 
        else
 
            right--; 
    }

    return false;
}

int main(){
    int arr[] = {0, -1, 2, -3, 1};
    int target = -2;
    int n = sizeof(arr) / sizeof(arr[0]);

    if (twoSum(arr, n, target))
        printf("true\n"); 
    else
        printf("false\n");

    return 0;
}