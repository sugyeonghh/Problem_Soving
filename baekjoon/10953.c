#include <stdio.h>

int main(void){
	int T;
    int A,B;
    scanf("%d",&T);
    int arr[T];
    for(int i=0; i<T; i++){
        scanf("%d,%d",&A,&B);
        arr[i]=A+B;
    }
    for(int i=0; i<T; i++){
        printf("%d \n",arr[i]);
    }
	return 0;
}
