//A vector in c++ is like a resizable array. 
//Both vecotors and arrays are data structures used to store multiple elements of the same data type.
//The difference between an array and a vector , is that the size of an array cannot be modified (you cannot add or remove elements from an array). A vector however, can grwo or shrink in size as needed.
//To use a vector, you have to include the <vector > header file:

// #include <iostream>
// #include <vector>
// using namespace std;

// //vector <type>vectorname

// int main(){
//     vector <string> cars={"volvo", "BMW", "Ford"};

//     for (string car: cars){
//         cout<<car<< "\n";
//         cout<<cars[0];
//         cout<<cars[1];
//         cout<<cars.front();
//         cout<<cars.back();
//         cout<<cars.at(1);
//         cout<<cars.at(0);
//         cars[0]="Opel";
//         cars.at(0)="Opel";
//         cout<<cars.at(0);
//         cars.push_back("Tesla");
//         cars.pop_back();
//         cout<<cars.size();
//         cout<<cars.empty();

//         for (int i=0; i<cars.size(); i++){
//             cout<<cars[i] << "\n";
//         }
//         //using more cleaner method

//         for (string car: cars){
//             cout<<car<< "\n";
//         }

//     }
// }

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string common="";
        sort(strs.begin(), strs.end());
        int n=strs.size();
        string first =strs[0], last=strs[n-1];
        for (int i=0; i<min(first.size(), last.size()); i++){
            if (first[i]!=last[i]){
                return common;
            }
            common+=first[i];
        }
       
        return common;
        
    }
};
int main(){
Solution sol;
vector <string> v={"flower", "flight", "flee"};
cout<< "The longest common prefix is : "<<sol.longestCommonPrefix(v)<<endl;

return 0;
}