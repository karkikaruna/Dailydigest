//Dynamic memory allocation
//memory allocation at runtime.

//malloc(): memory allocation
//takes number of bytes to be allcoatedand returns a pointer of type void.

// #include <stdio.h>
// #include <stdlib.h>
// int main(){
//     int *ptr;
//     ptr=(int*)malloc(5* sizeof(int));
//     ptr[0]=1;
//     ptr[1]=3;
//     ptr[2]=7;
//     ptr[4]=9;

//     for (int i=0; i<5; i++){
//         printf("%d\n", ptr[i] );
//     }
//     return 0;
// }

//calloc(): continuous allocation
//initializes with 0

// #include <stdio.h>
// #include <stdlib.h>
// int main(){
//     int *ptr;
//     ptr=(int*)calloc(5, sizeof(int));
//     // ptr[0]=1;
//     // ptr[1]=3;
//     // ptr[2]=7;
//     // ptr[4]=9;

//     for (int i=0; i<5; i++){
//         printf("%d\n", ptr[i] );
//     }
//     return 0;
// }

//WAP to allocate memory of size n 

// #include <stdio.h>
// #include <stdlib.h>

// int main(){
//     int *ptr, n;
//     printf("Enter size of memory: \n");
//     scanf("%d", &n);
//     ptr=(int*)malloc(n*sizeof(int));
//     for (int i=0; i<n; i++){
//         printf("%d\n", ptr[i]);

//     }
// return 0;
// }

// free(): we use it to free memory that is allocated using malloc and calloc

// #include <stdio.h>
// #include <stdlib.h>

// int main(){
//     int *ptr, n;
//     printf("Enter size of memory: \n");
//     scanf("%d", &n);
//     ptr=(int*)malloc(n*sizeof(int));
//     for (int i=0; i<n; i++){
//         printf("%d\n", ptr[i]);

//     }

//     free(ptr);
//      ptr=(int*)malloc(2*sizeof(int));
//     for (int i=0; i<2; i++){
//         printf("%d\n", ptr[i]);

//     }
// return 0;
// }

///realloc()
//reallocate (increase or decrease ) memory using the same pointer and size.

//ptr=realloc(ptr, newSize);


// #include <stdio.h>
// #include <stdlib.h>

// int main(){
//     int *ptr;
//     ptr=(int*) calloc(5, sizeof(int));

//     printf("Enter 5 numbers: \n");
//     for (int i=0; i<5; i++){
//         scanf("%d", &ptr[i]);
//     }

//     ptr=realloc(ptr, 8);
//     printf("Enter 8 nubers: ");
//     for (int i=0; i<8; i++){
//         scanf("%d\n", &ptr[i]);
//     }
//     for (int i=0; i<8; i++){
//         printf("Nuber %d is %d", i, ptr[i]);
//     }
//     return 0;

//}

#include <stdio.h>
#include <stdlib.h>

int main(){

    int *ptr;
    ptr=(int*) calloc(5, sizeof(int));
    ptr[0]=1;
    ptr[1]=3;
    ptr[2]=5;
    ptr[3]=7;
    ptr[4]=9;
    for (int i=0; i<5; i++){
    printf("%d\n", ptr[i]);
    }

    ptr=realloc(ptr, 6);
    ptr[0]=2;
    ptr[1]=4;
    ptr[2]=6;
    ptr[3]=8;
    ptr[4]=10;
    ptr[5]=12;

    for (int i=0; i<6; i++){
        printf("%d\n", ptr[i]);
    }
    free(ptr);
    return 0;

}
   

