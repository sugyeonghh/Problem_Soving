#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	N;
	int	max;
	int	*nums;
	int	*cnt;
	int	*sorted;

	scanf("%d", &N);
	nums = (int *)malloc(sizeof(int) * N);
	sorted = (int *)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
		scanf("%d", nums + i);
	max = 0;
	for (int i = 0; i < N; i++)
		if (max < nums[i])
			max = nums[i];
	cnt = (int *)calloc(max + 1, sizeof(int));
	for (int i = 0; i < N; i++)
		cnt[nums[i]]++;
	for (int i = 1; i < max + 1; i++)
		cnt[i] += cnt[i - 1];
	for (int i = N - 1; i >= 0; i--)
		sorted[--cnt[nums[i]]] = nums[i];
	for (int i = 0; i < N; i++)
		printf("%d\n", sorted[i]);
	return (0);
}
