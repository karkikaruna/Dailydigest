// // # 5}. Find the Longest
// // # Common Subsequence (LCS) between the strings “COMPANY” and “COLONY”.
#include <stdio.h>
#include <string.h>

int main(){
    char first []="COMPANY";
    char second []="COLONY";
    int i;
    char match[10];
    
    while (first[i]==second[i]){
    if (first[i]==second[i]){
        match[i]=first[i];
        
    }
    i++;
}
int length =0;
while (match[length] !='\0'){
    length ++;
}

printf("Length of matched strings is %d \n", length);
for (i=0; i<strlen(match); i++){
    printf("%c",match[i]);
    printf("\n");
}
return 0;
    
}
