#include <stdio.h>
#include <stdlib.h>

int		ft_compare(const void *a, const void *b)
{
	return (*(int *)a - *(int *)b);
}

int		main(void)
{
	int	N;
	int	*arr;

	scanf("%d", &N);
	arr = (int *)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)	
		scanf("%d", arr + i);
	qsort(arr, N, sizeof(int), ft_compare);
	for (int i = 0; i < N; i++)	
		printf("%d\n", arr[i]);
}