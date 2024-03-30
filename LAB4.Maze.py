def find_exit(matrix, start, end):
    n = len(matrix)

    stack = [start]  # Инициализируем стек начальной позицией

    # Массив для отслеживания посещенных клеток
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start[0]][start[1]] = True

    # Массив смещений для проверки всех возможных соседних клеток
    row_moves = [-1, 0, 0, 1]
    col_moves = [0, -1, 1, 0]

    while stack:

        current_row, current_col = stack.pop()

        # Если достигли выхода, завершаем поиск
        if (current_row, current_col) == end:
            print("Выход из лабиринта найден.")
            return True

        # Проверяем все соседние клетки
        for _ in range(4):
            next_row = current_row + row_moves[_]
            next_col = current_col + col_moves[_]

            if [next_row, next_col] == end:
                print("Выход из лабиринта найден.")
                return True

            if ((0 <= next_row < n) and (0 <= next_col < n) and matrix[next_row][next_col] == 0 and
                    not visited[next_row][next_col]):
                stack.append([next_row, next_col])
                visited[next_row][next_col] = True

    print("Выход из лабиринта не найден.")
    return False


maze = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]

a = [[0, 1], [14, 13]]

find_exit(maze, a[0], a[1])
