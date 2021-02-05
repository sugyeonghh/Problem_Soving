#include <stdio.h>

void	swap(int *x, int *y)
{
	int	tmp;

	tmp = *x;
	*x = *y;
	*y = tmp;
}

int		main(void)
{
	int	N;
	scanf("%d", &N);
	
	int	location[N][2];
	
	for (int i = 0; i < N; i++)
		scanf("%d %d", &location[i][0], &location[i][1]);
	for (int i = N - 1; i > 0; i--)
	{
		for (int j = 0; j < i; j++)
		{
			if ((location[j][0] == location[j + 1][0]) && (location[j][1] > location[j + 1][1]))
			{
				swap(&location[j][0], &location[j + 1][0]);
				swap(&location[j][1], &location[j + 1][1]);
			}
			else if (location[j][0] > location[j + 1][0])
			{
				swap(&location[j][0], &location[j + 1][0]);
				swap(&location[j][1], &location[j + 1][1]);
			}
		}
	}
	for (int i = 0; i < N; i++)
		printf("%d %d\n", location[i][0], location[i][1]);
	return (0);
}