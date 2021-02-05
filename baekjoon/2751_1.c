#include <stdio.h>
#include <stdlib.h>

void	merge(int *arr, int p, int q, int r)
{
	int	i;
	int	j;
	int	t;
	int	tmp[r];

	i = p;
	j = q + 1;
	t = 0;
	while (i <= q && j <= r)
		tmp[t++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
	while (i <= q)
		tmp[t++] = arr[i++];
	while (j <= r)
		tmp[t++] = arr[j++];
	i = p;
	t = 0;
	while (i <= r)
		arr[i++] = tmp[t++];
}

void	mergeSort(int *arr, int p, int r)
{
	int	q;

	if (p < r)
	{
		q = (p + r) / 2;
		mergeSort(arr, p, q);
		mergeSort(arr, q + 1, r);
		merge(arr, p, q, r);
	}
}

int		main(void)
{
	int	N;
	int	*arr;

	scanf("%d", &N);
	arr = (int *)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)	
		scanf("%d", arr + i);
	mergeSort(arr, 0, N - 1);
	for (int i = 0; i < N; i++)	
		printf("%d\n", arr[i]);
}
