#include <stdio.h>
#include <stdlib.h>
#define MAX(a, b) a > b ? a : b

int main(void) {
	int n;
	int *stairs;
	int *f;

	scanf("%d", &n);
	stairs = (int*)malloc(sizeof(int) * (n + 1));
	stairs[0] = 0;
	for (int i = 1; i <= n; i++)
		scanf("%d", &stairs[i]);
	f = (int*)malloc(sizeof(int) * (n + 1));
	f[0] = 0;
	f[1] = stairs[1];
	f[2] = MAX(stairs[2], stairs[1] + stairs[2]);
	for (int i = 3; i <= n; i++)
		f[i] = MAX(stairs[i] + stairs[i - 1] + f[i - 3], stairs[i] + f[i - 2]);
	printf("%d", f[n]);
	return 0;
}