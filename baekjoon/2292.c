#include <stdio.h>

int	main(void)
{
	int	N;
	int	range;
	int	cnt;

	scanf("%d", &N);
	range = 1;
	cnt = 1;
	while (range < N)
		range += 6 * cnt++;
	printf("%d", cnt);
	return (0);
}
