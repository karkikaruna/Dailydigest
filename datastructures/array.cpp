// #include <iostream>
// using namespace std;
// #include <climits>
// int main(){

//     //smallest and largest in Array

//     int nums[]={4, 1, 89, 99, 6};
//     int size=5;

//     int smallest =  INT_MAX;
//     int smallestindex=0;
//     int largest=INT_MIN;
//     int largestindex=0;

//     for (int i=0; i<size; i++){
//         if (smallest >nums[i]){
//             smallest=nums[i];
//             smallestindex=i;
//         }
//         if (largest <nums[i]){
//             largest =nums[i];
//             largestindex=i;
//         }
       
//     }
//      cout <<"smallest is "<<smallest<<"and index is "<<smallestindex<<endl;
//      cout <<"largest is "<<largest<<"and largest index is"<<largestindex<<endl;

//      return 0;

// }

//Pass by reference

// #include <iostream>
// using namespace std;

// void changeArr(int arr[], int size){
//     cout <<"in function\n";
//     for (int i=0; i<size; i++){
//         arr[i]=2*arr[i];
//     }
// }
// int main(){
//     int arr[]={1,2,4};
//     changeArr(arr, 3);
//     for (int i=0; i<3; i++){
//         cout<<arr[i]<<" ";
//     }
//     cout <<endl;


//     return 0;
// }


// #include <iostream>
// using namespace std;

// int linearsearch(int arr[], int size, int target){
//         for (int i=0; i<size; i++){
//         if (target==arr[i]){
//             cout <<"Target found!"<<"its index is: "<<i<<endl;
//             return i;

//         }
       
//     }
//     return -1;

// }
// void reversearray(int arr[], int size){
//     int start=0;
//     int end=size-1;
//     while (start<end){
//         swap(arr[start], arr[end]);
//         start++;
//         end--;
//     }

// }


// // int main(){

// //     int arr[]={4,2, 7, 8, 1, 2, 5};
// //     int target=8;
// //     int size=sizeof(arr)/sizeof(int);
    
// //     reversearray(arr, size);
// //     for(int i=0; i<size; i++){
// //         cout<<arr[i]<<" ";

// //     }
// //     cout<<endl;

// //     return 0;
// // }

// #include <iostream>
// using namespace std;
// int sum(int arr[], int size){
//     int summ=0;
//     for (int i=0; i<size;i++){
//         summ+=arr[i];
//     }
//     return summ;
// }

// int product (int arr[], int size){
//     int productt =1;
//     for (int i=0; i<size; i++){
//         productt=productt*arr[i];
//     }
//     return productt;
// }


// int main(){
//     int arr[]={8, 9, 5, 4, 3};
//     int size=sizeof(arr)/sizeof(int);

//     sum(arr, size);
//     product(arr, size);

//     cout <<"sum is: "<<sum(arr, size)<<endl;
//     cout<<"product is: "<<product(arr, size)<<endl;

//     return 0;
// }

//swap max and min number in an array
