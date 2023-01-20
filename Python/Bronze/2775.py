for _ in range(int(input())):
    k, n = int(input()), int(input()) # k층 n호 / 1층 3호 -> 6명 (0층 1호, 2호, 3호)
    array = [[0] * (n+1) for _ in range(k+1)]

    for i in range(1, n+1):
        array[0][i] = i

    for i in range(1, k+1):
        for j in range(1, n+2):
            array[i][j-1] = sum(array[i-1][:j])

    print(array[k][n])
