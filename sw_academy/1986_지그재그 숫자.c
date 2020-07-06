#include <stdio.h>

main(){
    int test;
    int num;
    int sum=0;
    
    scanf("%d",&test);
    
    for(int i=0; i<test; i++){
        scanf("%d", &num);
        for(int j=1;j<=num;j++){
            if(j%2!=0){ //홀수
                sum+= j;
            }else{ //짝수
				sum -= j;
            }
   		}
        printf("#%d %d \n",i+1,sum);
        sum=0;
    }
            
}