#include <stdio.h>
#include <stdlib.h>

int	find_arr(char **board, int x, int y, char *compare1, char *compare2)
{
	int idx;
	int cnt = 0;

	for (int i = x; i < x + 8; i++)
	{
		idx = 0;
		for (int j = y; j < y + 8; j++)
		{
			if (!(i % 2))
			{
				if (board[i][j] != compare1[idx])
					cnt++;
			}
			else
			{
				if (board[i][j] != compare2[idx])
					cnt++;
			}
			idx++;
		}
	}
	return (cnt);
}

int	main(void)
{
	int	N, M;
	char *start_W = "WBWBWBWB";
	char *start_B = "BWBWBWBW";
	int	cnt = 0, res = 0;
	char **board;

	scanf("%d %d", &N, &M);
	res = N * M;
	board = (char**)malloc(sizeof(char*) * N);
	for (int i = 0; i < N; i++)
		board[i] = (char*)malloc(sizeof(char) * M);

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			scanf(" %c", &board[i][j]);

	for (int i = 0; i < N; i++)
	{
		cnt = 0;
		for (int j = 0; j < M; j++)
		{
			if ((i + 7 >= N) || (j + 7 >= M))
				continue;
			int W = find_arr(board, i, j, start_W, start_B);
			int B = find_arr(board, i, j, start_B, start_W);
			cnt = W < B ? W : B;
			res = cnt < res ? cnt : res;
		}
	}
	printf("%d", res);
	return (0);
}
