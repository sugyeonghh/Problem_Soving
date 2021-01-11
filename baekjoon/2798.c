#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int N, M;
	int *card;
	int sum;

	scanf("%d %d", &N, &M);
	card = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
		scanf("%d", card + i);
	sum = 0;
	for (int i = 0; i < N - 2; i++)
	{
		for (int j = i + 1; j < N - 1; j++)
		{
			for (int k = j + 1; k < N; k++)
			{
				int tmp;
				tmp = card[i] + card[j] + card[k];
				if (tmp > M)
					continue;
				else
				{
					if (sum < tmp)
						sum = tmp;
				}
			}
		}
	}
	printf("%d", sum);
	return (0);
}