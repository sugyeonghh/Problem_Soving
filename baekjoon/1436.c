#include <stdio.h>
#include <stdlib.h>

int	is_pattern(int num)
{
	int	cnt;

	cnt = 0;
	while (num)
	{
		if (num % 10 == 6)
			cnt++;
		else if (cnt < 3)
			cnt = 0;
		num /= 10;
		if (cnt == 3)
			return (1);
	}
	return (0);
}

int	main(void)
{
	int	N;
	int	num = 0;
	int cnt = 0;
	
	scanf("%d", &N);
	while (1)
	{
		if (cnt == N)
			break ;
		if (is_pattern(num++))
			cnt++;
	}
	printf("%d", num - 1);
	return (0);
}