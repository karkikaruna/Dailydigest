#include <iostream>
using namespace std;
#include <unordered_map>

int main(){

    unordered_map<int, string> um= { 
        {1, "hi"}, {2, "hello"}, {3, "bye"}
    };

    for (auto i: um)
        cout<<i.first<< ": "<<i.second<<endl;
        return 0;

}
