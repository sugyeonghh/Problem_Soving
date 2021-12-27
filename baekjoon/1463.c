#include <stdio.h>
#include <stdlib.h>
#define MIN(a, b) a < b ? a : b

int main(void) {
	int n;
	int *arr;

	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int) * (n + 1));
	arr[0] = arr[1] = 0;
	arr[2] = arr[3] = 1;
	for (int i = 4; i < n + 1; i++) {
		if (i % 2 == 0 && i % 3 == 0)
			arr[i] = (MIN(MIN(arr[i / 2], arr[i / 3]), arr[i - 1])) + 1;
		else if (i % 2 == 0)
			arr[i] = (MIN(arr[i / 2], arr[i - 1])) + 1;
		else if (i % 3 == 0)
			arr[i] = (MIN(arr[i / 3], arr[i - 1])) + 1;
		else 
			arr[i] = arr[i - 1] + 1;
	}
	printf("%d\n", arr[n]);
	free(arr);
	return 0;
}