#include <stdio.h>
#define N 10001

int		d(int n)
{
	int	sum;

	sum = n;
	while (n)
	{
		sum += (n % 10);
		n /= 10;
	}
	return (sum);
}

int		main(void)
{
	int	nums[N] = {0,};
	int idx;

	for (int i = 1; i < N; i++)
		if ((idx = d(i)) < N)
			nums[idx] = 1;
	for (int i = 1; i < N; i++)
		if (!nums[i])
			printf("%d\n", i);
	return (0);
}
