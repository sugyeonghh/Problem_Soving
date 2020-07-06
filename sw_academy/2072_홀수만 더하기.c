#include <stdio.h>

main(){
 	int t;
    int sum=0;
    int num=0;
    scanf("%d",&t);
    for(int i=0; i<t; i++){
        for(int j=0; j<10; j++){
      	 	scanf("%d", &num);
            if(num % 2 == 1){
                sum+=num;
            }
        }
        printf("#%d %d \n", i+1, sum);
        sum=0;
    }
}