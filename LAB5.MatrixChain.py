def matrix_chain_multiplication(matrix_chain):
    n = len(matrix_chain)

    # Создаем матрицу m
    # Строки m[i][0] и столбцы m[0][j] не будут использоваться
    m = [[0 for x in range(n)] for x in range(n)]

    for i in range(2, n):
        m[i][i] = 0

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1

            # максимальное число для сравнения
            m[i][j] = int(1e9 + 7)

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + matrix_chain[i - 1] * matrix_chain[k] * matrix_chain[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n-1]


result = matrix_chain_multiplication([2, 1, 2, 3, 4])
print(result)
