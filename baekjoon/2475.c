#include <stdio.h>
#include <math.h>

int main(void) {
	int arr[5] = {0, };
	int res = 0;

	for (int i = 0; i < 5; i++) 
		scanf("%d", arr + i);
	for (int i = 0; i < 5; i++)
		res += pow(arr[i], 2);
	printf("%d\n", res % 10);	
	return 0;
}