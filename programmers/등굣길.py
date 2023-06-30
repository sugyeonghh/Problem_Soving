def solution(m, n, puddles):
    graph = [[0 for i in range(m + 1)] for j in range(n + 1)]
    graph[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] not in puddles:
                a = graph[i - 1][j]
                b = graph[i][j - 1]
                graph[i][j] += a if a > 0 else 0
                graph[i][j] += b if b > 0 else 0
    return graph[n][m] % 1000000007