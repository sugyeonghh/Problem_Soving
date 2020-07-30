#include <stdio.h>

int main(void){
    int sum=0;
    int score[5];
    scanf("%d", &score[0]);
    scanf("%d", &score[1]);
    scanf("%d", &score[2]);
    scanf("%d", &score[3]);
    scanf("%d", &score[4]);

    for(int i=0; i<5; i++){
        if(score[i]<40)
            score[i]=40;
        sum+=score[i];
    }

    printf("%d", sum/5);
    return 0;
}