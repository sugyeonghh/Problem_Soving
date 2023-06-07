def solution(board):
    n = len(board)
    pos = set([])
    
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, -1, 0, 1, 0, -1]
    
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 1:
                for x, y in zip(dx, dy):
                    if 0 <= i + x < n and 0 <= j + y < n: 
                        pos.add((i + x, j + y))
    return n * n - len(pos)