def compute():
    with open('p081_matrix.txt', 'r') as f:
        grid = [[int(num) for num in line.split(',')] for line in f]

    for i in reversed(range(len(grid))):
        for j in reversed(range(len(grid[i]))):
            if i + 1 < len(grid) and j + 1 < len(grid[i]):
                temp = min(grid[i + 1][j],grid[i][j + 1])
            elif i + 1 < len(grid):
                temp = grid[i + 1][j]
            elif j + 1 < len(grid[i]):
                temp = grid[i][j + 1]
            else:
                temp = 0
            grid[i][j] += temp

    return grid[0][0]

if __name__ == "__main__":
    print(compute())
