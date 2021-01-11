#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	N;
	int	*weight;
	int	*high;
	int	k;
	int	*res;

	scanf("%d", &N);
	weight = (int*)malloc(sizeof(int) * N);
	high = (int*)malloc(sizeof(int) * N);
	res = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
		scanf("%d %d", weight + i, high + i);
	for (int i = 0; i < N; i++)
	{
		k = 0;
		for (int j = 0; j < N; j++)
		{
			if (i == j)
				continue;
			if ((weight[i] < weight[j]) && (high[i] < high[j]))
				k++;
		}
		res[i] = k + 1;
	}
	for (int i = 0; i < N; i++)
		printf("%d ", res[i]);
	return (0);
}
