// #include <stdio.h>
// #include <string.h>
// #include <stdlib.h>

// char *strrev(char *str){
//     int len=strlen(str);

//     char *rev =(char *) malloc(sizeof(char)* (len+1));
//     for(int i=0; i<len; i++){
//         rev[i]=str[len-i-1];

//     }
//     rev[len]='\0';
//     return rev;
// }

// void isPalindrome(char *str){
//     char *rev=strrev(str);
//     if (strcmp(str, rev)==0)
//         printf("\"%s\" is palindrome.\n", str);
//     else
//         printf("\"%s\"is not palindrome.\n", str);

// }
// int main(){
//     isPalindrome("madam");
//     isPalindrome("hello");
// }

// #include <stdio.h>
// #include <string.h>
// #include <stdbool.h>

// void isPalindrome(char *str){
//     int left=0;
//     int right =strlen(str)-1;

//     while (left<right){
//         if(str[left]!=str[right]){
//             printf("\"%s\"is not palindrome.\n", str);
//             return;

//         }
//         left ++;
//         right --;
//     }
//     printf("\"%s\" is palindrome.\n", str);

// }
// int main(){
//     isPalindrome("madam");
//     isPalindrome("hello");
//     return 0;
// }

//using =recursion

// #include <stdio.h>
// #include <string.h>
// #include <stdbool.h>

// bool palinHelper(char *s, int left, int right){
//     if (left>=right)
//         return true;
//     if (s[left]!=s[right])
//         return false;
//     return palinHelper(s, left+1, right-1);
// }
// void isPalindrome(char *s){
//     if(palinHelper(s, 0, strlen(s)-1))
//     printf("\"%s\" is palindrome.\n", s);
//     else
//         printf("\"%s\" isnot palindrome. \n", s);

// }
// int main(){
//     isPalindrome("madam");
//     isPalindrome("hello");
//     return 0;
// }