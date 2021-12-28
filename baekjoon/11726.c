#include <stdio.h>
#define MAX_SIZE 1001

int main(void) {
	int n;
	int fib[MAX_SIZE] = {0, };

	scanf("%d", &n);
	fib[1] = 1;
	fib[2] = 2;
	for (int i = 3; i <= n; i++)
		fib[i] = (fib[i - 1] + fib[i - 2]) % 10007;
	printf("%d \n", fib[n]);
	return 0;
}