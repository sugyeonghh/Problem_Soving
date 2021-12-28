#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 1001

void dfs(int graph[][MAX_SIZE], int vertex, int *visited, int v, int cnt) {
	visited[v] = cnt;
	for (int u = 0; u <= vertex; u++) {
		if (graph[v][u] && !visited[u])
			dfs(graph, vertex, visited, u, cnt);
	}
}

void find_connected_component(int graph[][MAX_SIZE], int vertex, int *visited, int v) {
	int cnt = 0;
	for (int u = 1; u <= vertex; u++) {
		if (!visited[u]) {
			cnt++;
			dfs(graph, vertex, visited, u, cnt);
		}
	}
	printf("%d \n", cnt);
}

int main(void) {
	int vertex, edge;
	int graph[MAX_SIZE][MAX_SIZE] = {0, };
	int visited[MAX_SIZE] = {0, };

	scanf("%d %d", &vertex, &edge);
	for (int i = 0; i < edge; i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		graph[u][v] = 1;
		graph[v][u] = 1;
	}
	find_connected_component(graph, vertex, visited, 1);
	return 0;
}