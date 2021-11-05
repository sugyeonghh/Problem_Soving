#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int num = 0;
	int *arr;
	int cnt = 0;
	int s, e;
	
	scanf("%d", &num);
	arr = (int*)calloc(num, sizeof(int));
	for (int i = 0; i < num; i++) 
		scanf("%d", arr + i);
	s = 0;
	e = num - 1;
	while (s < num - 1) {
		if (arr[s] == arr[e] && arr[s] < arr[s + 1]) {
			cnt++;
			e--;
		}
		else {
			cnt = 0;
			e = num - 1;
		}
		s++;
	}
	printf("%d \n", cnt);
	return 0;
}
