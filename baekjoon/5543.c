#include <stdio.h>

int main(void){
    int sangduk,jungduk,haduk,coke,cider;
    int hambuger=0, drink;
    scanf("%d",&sangduk);
    scanf("%d",&jungduk);
    scanf("%d",&haduk);
    scanf("%d",&coke);
    scanf("%d",&cider);

    if(sangduk<jungduk){
        hambuger = sangduk<haduk ? sangduk : haduk;
    }else{
        hambuger = jungduk<haduk ? jungduk : haduk;
    }
    drink = coke<cider ? coke : cider;

    printf("%d",hambuger+drink-50);
	return 0;
}
