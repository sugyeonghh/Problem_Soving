#include <stdio.h>

main(){
    int t=0;
    int N=0;
    int a=0, b=0, c=0, d=0, e=0;
    scanf("%d", &t);
    for(int cnt=0; cnt<t; cnt++){
        scanf("%d", &N);
        while(N!=0){
            if(N%2==0){
                N=N/2;
                a++;
            }else if(N%3==0){
                N=N/3;
                b++;
            }else if(N%5==0){
                N=N/5;
                c++;
            }else if(N%7==0){
                N=N/7;
                d++;
            }else if(N%11==0){
                N=N/11;
                e++;
            }else{
                break;
            }
        }
        printf("#%d %d %d %d %d %d \n", cnt+1 ,a,b,c,d,e);
        a=0, b=0, c=0, d=0, e=0;
    }
}