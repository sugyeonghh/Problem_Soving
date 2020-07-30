#include <stdio.h>

int main(void){
	int N;
	int cycle=0;
	scanf("%d",&N);
	int new = N;
	while(1){
		int ten = new>=10 ? new/10 : 0;
		int one = new%10;
		int result = ten+one;
		int new_one = result%10;
		new = one*10+new_one;
		cycle++;
		if(new == N)
			break; 

	}
	printf("%d", cycle);
	return 0;
}
