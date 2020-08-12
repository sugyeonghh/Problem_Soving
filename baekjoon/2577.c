#include <stdio.h>

int main(void){
    int num[10]={0,};
    int A,B,C,result;
    scanf("%d %d %d",&A,&B,&C);
    result = A*B*C;
    while(result>0){
        int number = result%10;
        switch(number){
        case 0:
            num[0]+=1;
            break;
        case 1:
            num[1]+=1;
            break;
        case 2:
            num[2]+=1;
            break;
        case 3:
            num[3]+=1;
            break;
        case 4:
            num[4]+=1;
            break;
        case 5:
            num[5]+=1;
            break;
        case 6:
            num[6]+=1;
            break;
        case 7:
            num[7]+=1;
            break;
        case 8:
            num[8]+=1;
            break;
        case 9:
            num[9]+=1;
            break;
        }
        result = result/10;        
    }
    
    for(int i=0; i<10; i++){
        printf("%d \n", num[i]);
    }

    return 0;
}