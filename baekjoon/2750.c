#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	N;
	int	*nums;
	int	min;
	int	tmp;

	scanf("%d", &N);
	nums = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
		scanf("%d", nums + i);
	for (int i = 0; i < N - 1; i++)
	{
		min = i;
		for (int j = i + 1; j < N; j++)
		{
			if (nums[j] < nums[min])
				min = j;
		}
		tmp = nums[i];
		nums[i] = nums[min];
		nums[min] = tmp;
	}
	for (int i = 0; i < N; i++)
		printf("%d\n", nums[i]);
	return (0);
}