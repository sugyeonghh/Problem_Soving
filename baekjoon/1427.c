#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	N;
	int	tmp;
	int	*nums;
	int	len = 0;

	scanf("%d", &N);
	tmp = N;
	while (tmp)
	{
		tmp /= 10;
		len++;
	}
	nums = (int *)malloc(sizeof(int) * len);
	for (int i = 0; i < len; i++)
	{
		nums[i] = N % 10;
		N /= 10;
	}
	for (int i = len - 1; i > 0; i--)
	{
		for (int j = 0; j < i; j++)
		{
			if (nums[j] < nums[j + 1])
			{
				tmp = nums[j];
				nums[j] = nums[j + 1];
				nums[j + 1] = tmp;
			}
		}
	}
	for (int i = 0; i < len; i++)
		printf("%d", nums[i]);
	return (0);
}
