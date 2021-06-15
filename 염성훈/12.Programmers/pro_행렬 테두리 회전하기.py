def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1
    for row in range(rows):
        for column in range(columns):
            arr[row][column] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        tmp = arr[x1 - 1][y1 - 1]
        mini = tmp

        for k in range(x1 - 1, x2 - 1):
            test = arr[k + 1][y1 - 1]
            arr[k][y1 - 1] = test
            mini = min(mini, test)

        for k in range(y1 - 1, y2 - 1):
            test = arr[x2 - 1][k + 1]
            arr[x2 - 1][k] = test
            mini = min(mini, test)

        for k in range(x2 - 1, x1 - 1, -1):
            test = arr[k - 1][y2 - 1]
            arr[k][y2 - 1] = test
            mini = min(mini, test)

        for k in range(y2 - 1, y1 - 1, -1):
            test = arr[x1 - 1][k - 1]
            arr[x1 - 1][k] = test
            mini = min(mini, test)

        arr[x1 - 1][y1] = tmp
        answer.append(mini)

    return answer

rows = 6
columns = 6
queries = [[2, 2, 5, 4],[3, 3, 6, 6], [5, 1, 6, 3]]

solution(rows, columns, queries)