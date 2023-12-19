# Matrix Chain Multiplication
def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

# Example usage
matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain_order(matrix_dimensions)
print("Minimum number of multiplications:", m[0][-1])
