#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int line, station, arrival;
	int **graph;

	scanf("%d", &line);
	graph = (int**)malloc(sizeof(int*) * (line + 1));
	for (int i = 0; i <= line; i++) {
		scanf("%d", &station);
		graph[i] = (int*)malloc(sizeof(int) * station);
		for (int j = 1; j < station; j++) {
			int s;
			scanf("%d", &s);
			graph[i][j] = s;
		}
	}
	scanf("%d", &arrival);


}