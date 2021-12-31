#include <stdio.h>
#define MAX 1001

int main(void) {
	int n;
	int arr[MAX] = {0, };
	int pos = 0;

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int tmp;
		scanf("%d", &tmp);
		if (tmp > arr[pos])
			arr[++pos] = tmp;
	}
	printf("%d\n", pos);
	return 0;
}