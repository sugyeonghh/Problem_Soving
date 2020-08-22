#include <stdio.h>

main(){
    int t;
    int max=0, min=10000; 
    int sum=0;
    int num[10];
    scanf("%d", &t);
    for(int cnt=0; cnt<t; cnt++){
        int min_t, max_t;
        for(int i=0; i<10; i++){
            scanf("%d", &num[i]);
            if(num[i]<min){
                min=num[i];
                min_t=i;
            }
            if(num[i]>max){
                max=num[i];
                max_t=i;
            }
        }
        num[min_t]=0, num[max_t]=0;
        for(int i=0; i<10; i++){
            sum+=num[i];
        }
        printf("#%d %d \n", cnt+1, (int)(sum/8.0+0.5));
        sum=0;
        max=0, min=10000;
    }    
}