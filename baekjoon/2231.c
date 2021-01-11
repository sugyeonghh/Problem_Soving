#include <stdio.h>

int ft_add(int num)
{
	if (num == 0)
		return (0);
	return (num % 10 + ft_add(num / 10));
}

int main(void)
{
	int N;
	int i;

	scanf("%d", &N);
	i = 0;
	while (i < N)
	{
		if ((i + ft_add(i)) == N)
			break ;
		i++;
	}
	if ((i + ft_add(i)) > N)
		i = 0;
	printf("%d", i);
	return (0);
}