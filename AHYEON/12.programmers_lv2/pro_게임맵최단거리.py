from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(maps):
    r = len(maps)
    c = len(maps[0])
    table = [[-1 for _ in range(c)] for _ in range(r)]
    q = deque()
    q.append([0,0])
    table[0][0] = 1

    while q:
        y, x = q.popleft()

        for mode in range(4):
            ny = y + dx[mode]
            nx = x + dy[mode]

            if -1 < ny < r and -1 < nx < c:
                if maps[ny][nx] == 1:
                    if table[ny][nx] == -1:
                        table[ny][nx] = table[y][x] + 1
                        q.append([ny, nx])

    answer = table[-1][-1]

    return answer
