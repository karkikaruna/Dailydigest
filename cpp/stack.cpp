//A stack stores multiple elements in a specific order, called LIFO
//LIFO stands for Last in , First Out. To visualize LIFO, think of a pile of pancakes, where 
//pancakes are both added and removed from the top. So when removing a pancake,
//it will always be the last one you added. This way of organizing elements is called LIFO in computer science and programming.

//unlike vectors, elements in the stack are not accessed by index numbers. since elements are 
//added and removed from the top, you can only access the element at the top of the stack.
//To use a stack, you have to include the <stack >header file:

#include <iostream>
using namespace std;
#include <stack>

//stack<type> stackName
int main(){
    stack <string> cars= {"volve", "BMW", "Ford", "Mazda"};
    cars.push("Volvo");
    cars.push("BMW");
    cars.push("mercedes");
    cout <<cars.top();
    cars.top()="Tesla";
    cout<<cars.top();
    cout <<cars.size();
    cout<<cars.empty();
}