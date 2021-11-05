#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int n;
	int num[10001] = {0, };
	int i = 0;

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int tmp;
		scanf("%d", &tmp);
		num[tmp] += 1;
	}
	
	while (i < 10001) {
		if (num[i] > 0) {
			printf("%d\n", i);
			num[i] -= 1;
		}
		else if (num[i] == 0)
			i++;
	}
	return 0;
}
