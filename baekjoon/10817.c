#include <stdio.h>

int main(void){
    int A,B,C;
    int result;
    scanf("%d %d %d",&A,&B,&C);

    if(A>=B){
        result = B>=C ? B : A>=C ? C : A;
    }else{
        result = A>=C ? A : B>=C ? C : B;
    }
    
    printf("%d",result);
    return 0;
}