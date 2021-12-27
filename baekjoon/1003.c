#include <stdio.h>

int main(void) {
	int t;
	int f0[41] = {0, };
	int f1[41] = {0, };

	f0[0] = f1[1] = 1;
	f0[1] = f1[0] = 0;
	for (int i = 2; i < 41; i++) {
		f0[i] = f0[i - 1] + f0[i - 2];
		f1[i] = f1[i - 1] + f1[i - 2];
	}
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int n;
		
		scanf("%d", &n);
		printf("%d %d\n", f0[n], f1[n]);
	}
	return 0;
}