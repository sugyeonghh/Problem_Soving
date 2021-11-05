#include <stdio.h>

int main(void) {
	int min, max;
	int arr[1000001] = {0, };

	scanf("%d %d", &min, &max);
	arr[1] = 1;
	for (int i = 2; i <= max; i++) {
		for (int j = 2; i * j <= max; j++) {
			arr[i * j] = 1;
		}
	}
	for (int i = min; i <= max; i++) {
		if (arr[i] == 0)
			printf("%d\n", i);
	}
	return 0;
}