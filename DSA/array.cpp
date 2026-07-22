// #include <iostream>
// using namespace std;

// //pass by reference
// //array is a non-primitive data type

// void changeArr(int arr[], int size){
//     for (int i=0; i<size; i++){
//         arr[i]=2*arr[i];
//     }
// }

// int linearSearch(int arr[], int sz, int target){
//     for (int i=0; i<sz; i++){
//         if (arr[i]==target){
//             return i;
//         }
//     }
//     return -1;
// }

// //reverse an array



// int main(){
//     int arr[]={1,3,4};
//     changeArr(arr, 3);
//     int size=3;

//     for (int i=0; i<size; i++){
//         cout<<arr[i] <<" ";
//     }
//     cout<<endl;
//     return 0;

// }

//rever9se an array

#include <iostream>
using namespace std;

void reverse( int arr[], int size){
    int start=0, end=size-1;
    while (start<end){
        swap(arr[start], arr[end]);
        start++;
        end--;
    }
}

int main(){
    int arr[]={1,3,4,5};
    int size=4;

    reverse(arr, size);

    for (int i=0;i<size; i++){
        cout<<arr[i] <<" " ;
    }
    cout<<endl;
    return 0;
}


