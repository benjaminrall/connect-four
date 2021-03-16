import copy

def reset():
    grid = [["O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O"]]
    return grid

def addValid(column, counter, grid):
    valid = False
    for i in range(len(grid)):
        r = (i * -1) + (len(grid) - 1)
        if grid[r][column - 1] == "O":
            valid = True
            if counter == 0:
                grid[r][column - 1] = "P"
                break
            else:
                grid[r][column - 1] = "C"
                break
    return grid, valid

def add(column, counter, grid):
    for i in range(len(grid)):
        r = (i * -1) + (len(grid) - 1)
        if grid[r][column - 1] == "O":
            if counter == 0:
                grid[r][column - 1] = "P"
                break
            else:
                grid[r][column - 1] = "C"
                break
    return grid

def row(grid):
    newGrid = []
    for row in grid:
        newGrid.append(" ".join(*zip(*row)))
    return newGrid

def print(grid):
    tempGrid = copy.deepcopy(grid)
    for r in range(len(tempGrid)):
        for i in range(len(tempGrid[r])):
            if tempGrid[r][i] == "O":
                tempGrid[r][i] = " "
    rows = row(tempGrid)
    newGrid = ""
    for i in range(len(rows)):
        newGrid += (rows[i] + "\n")
    newGrid += "1 2 3 4 5 6 7"
    return newGrid
