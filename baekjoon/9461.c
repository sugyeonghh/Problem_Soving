#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 101

int main(void) {
	long long dp[101] = {0, 1, 1, };
	int n;

	for (int i = 3; i < MAX_SIZE; i++)
		dp[i] = dp[i - 2] + dp[i - 3];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int tmp;
		scanf("%d", &tmp);
		printf("%lld\n", dp[tmp]);
	}
	return 0;
}