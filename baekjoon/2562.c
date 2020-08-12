#include <stdio.h>

int main(void){
    int numList[9];
    int max = 0;
    int index = 0;

    for(int i=0; i<9; i++){
        scanf("%d",&numList[i]);
    }

    for(int i=0; i<9; i++){
        if(numList[i]>max){
            max = numList[i];
            index = i+1;
        }
    }
    printf("%d\n%d",max,index);
    return 0;
}