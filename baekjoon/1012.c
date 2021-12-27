#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 50

void dfs(int graph[][MAX_SIZE], int vertex, int *visited, int v, int cnt) {
	visited[v] = cnt;
	printf("%d ", v);
	for (int u = 0; u < vertex; u++) {
		if (graph[v][u] && !visited[u])
			dfs(graph, vertex, visited, u, cnt);
	}
}

void find_connected_component(int graph[][MAX_SIZE], int vertex, int *visited, int v) {
	int cnt = 0;
	for (int u = 0; u < vertex; u++) {
		if (!visited[u]) {
			cnt++;
			dfs(graph, vertex, visited, u, cnt);
			printf("\n\n");
		}
	}
	printf("%d\n", cnt);
}

int main(void) {
	int t;
	int graph[MAX_SIZE][MAX_SIZE] = {0, };
	int visited[MAX_SIZE] = {0, };

	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int row, col, vertex;
		scanf("%d %d %d", &row, &col,&vertex);
		for (int j = 0; j < vertex; j++) {
			int x, y;
			scanf("%d %d", &x, &y);
			graph[y][x] = 1;
		}
		printf("\n");
		for (int a = 0; a < col; a++) {
			for (int b = 0; b < row; b++) {
				printf("%d ", graph[a][b]);
			}
			printf("\n");
		}
		printf("\n");
		find_connected_component(graph, vertex, visited, 0);
	}
	return 0;
}