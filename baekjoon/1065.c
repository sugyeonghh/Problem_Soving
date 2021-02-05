#include <stdio.h>

int		han_number(int N)
{
	int hundreds;
	int tens;
	int units;
	int cnt;

	if (N < 100)
		return (N);
	cnt = 99;
	for (int i = 100; i <= N; i++)
	{
		hundreds = i / 100;
		tens = (i / 10) % 10;
		units = i % 10;
		if ((hundreds - tens) == (tens - units))
			cnt++;
	}
	return (cnt);
}

int		main(void)
{
	int N;

	scanf("%d", &N);
	printf("%d", han_number(N));
}
