import sys

# Parse the arguments
n = int(sys.argv[1])
num_cells = int(sys.argv[2])
cells = [(int(x), int(y)) for x, y in (cell.split(',') for cell in sys.argv[3:])]

# Initialize the grid and set the initial live cells
grid = [[0 for _ in range(n)] for _ in range(n)]
for x, y in cells:
    grid[x][y] = 1

# Iterate through the grid and apply the rules of the Game of Life
while True:
    # Print the grid
    for row in grid:
        print(' '.join([str(cell) for cell in row]))
    print()

    # Count the number of live neighbors for each cell
    neighbors = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i > 0:
                neighbors[i][j] += grid[i-1][j]
            if i < n-1:
                neighbors[i][j] += grid[i+1][j]
            if j > 0:
                neighbors[i][j] += grid[i][j-1]
            if j < n-1:
                neighbors[i][j] += grid[i][j+1]
            if i > 0 and j > 0:
                neighbors[i][j] += grid[i-1][j-1]
            if i < n-1 and j < n-1:
                neighbors[i][j] += grid[i+1][j+1]
            if i > 0 and j < n-1:
                neighbors[i][j] += grid[i-1][j+1]
            if i < n-1 and j > 0:
                neighbors[i][j] += grid[i+1][j-1]

    # Update the grid based on the number of live neighbors
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 and neighbors[i][j] == 3:
                grid[i][j] = 1
            elif grid[i][j] == 1 and (neighbors[i][j] < 2 or neighbors[i][j] > 3):
                grid[i][j] = 0
