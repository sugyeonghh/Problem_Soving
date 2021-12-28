#include <stdio.h>
#include <stdlib.h>
#define MAX 100000

int main(void) {
	int n;
	int stack[MAX] = {0, };
	int top = -1;
	int sum = 0;

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int tmp;
		scanf("%d", &tmp);
		if (tmp != 0)
			stack[++top] = tmp;
		else
			top--;
	}
	for (int i = 0; i <= top; i++)
		sum += stack[i];
	printf("%d \n", sum);
	return (0);
}