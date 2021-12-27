#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 1001

void dfs(int graph[][MAX_SIZE], int vertex, int *visited, int v) {
	visited[v] = 1;
	printf("%d ", v);
	for (int u = 0; u < vertex + 1; u++) {
		if (graph[v][u] && !visited[u])
			dfs(graph, vertex, visited, u);
	}
}

void bfs(int graph[][MAX_SIZE], int vertex, int *visited, int v) {
	int queue[MAX_SIZE] = {0, };
	int front = -1, rear = -1;
	visited[v] = 1;
	printf("%d ", v);
	queue[++rear] = v;
	while ((rear >= 0) && (front < rear)) {
		v = queue[++front];
		for (int u = 0; u < vertex + 1; u++) {
			if (graph[v][u] && !visited[u]){
				visited[u] = 1;
				printf("%d ", u);
				queue[++rear] = u;
			}
		}
	}
}

int main(void) {
	int vertex, edge, v;
	int graph[MAX_SIZE][MAX_SIZE] = {0, };
	int visited[MAX_SIZE] = {0, };

	scanf("%d %d %d", &vertex, &edge, &v);
	for (int i = 0; i < edge; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		graph[a][b] = 1;
		graph[b][a] = 1;
	}
	dfs(graph, vertex, visited, v);
	printf("\n");
	memset(visited, 0, sizeof(int) * MAX_SIZE);
	bfs(graph, vertex, visited, v);
	printf("\n");
	return 0;
}