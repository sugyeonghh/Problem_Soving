#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAX_SIZE 101

void dfs(int graph[][MAX_SIZE], int vertex, int *visited, int v, int *cnt) {
	visited[v] = 1;
	(*cnt) += 1;
	for (int i = 0; i < vertex + 1; i++) {
		if (graph[v][i] && !visited[i])
			dfs(graph, vertex, visited, i, cnt);
	}
}

int main(void) {
	int vertex, edge;
	int graph[MAX_SIZE][MAX_SIZE] = {0, };
	int visited[MAX_SIZE] = {0, };
	int cnt = 0;

	scanf("%d", &vertex);
	scanf("%d", &edge);
	for (int i = 0; i < edge; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		graph[a][b] = 1;
		graph[b][a] = 1;
	}
	dfs(graph, vertex, visited, 1, &cnt);
	printf("%d \n", cnt - 1);
	return 0;
}