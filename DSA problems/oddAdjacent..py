def oddAdjacent(matrix: list[list]) -> list[list]:
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if checkAdj(i, j, rows, cols):
                matrix[i][j] = -matrix[i][j]

    return matrix


def checkAdj(i, j, rows, cols) -> bool:
    count = 0

    if i > 0:
        elem = matrix[i - 1][j]
        if elem % 2 == 1:
            count += 1

    if j > 0:
        elem = matrix[i][j - 1]
        if elem % 2 == 1:
            count += 1

    if i < rows - 1:
        elem = matrix[i + 1][j]
        if elem % 2 == 1:
            count += 1

    if j < cols - 1:
        elem = matrix[i][j + 1]
        if elem % 2 == 1:
            count += 1

    return count >= 2


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = oddAdjacent(matrix)
print(ans)
