import grids, copy

def checkDraw(grid):
    draw = True
    for row in grid:
        for item in row:
            if item == "O":
                draw = False
    return draw

def getPlayer(player):
    if player == 0:
        return "P"
    elif player == 1:
        return "C"
    return "O"

def checkHorizontalWin(grid, player):
    player = getPlayer(player)
    for row in grid:
        inRow = 0
        for item in row:
            if item == player:
                inRow += 1
            elif item != player and inRow < 4:
                inRow = 0
        if inRow >= 4:
            return True
    return False

def checkVerticalWin(grid, player):
    player = getPlayer(player)
    for column in range(len(grid[0])):
        inRow = 0
        for row in range(len(grid)):
            if grid[row][column] == player:
                inRow += 1
            elif grid[row][column] != player and inRow < 4:
                inRow = 0
        if inRow >= 4:
            return True
    return False

def checkDiagonalWin(grid, player):
    player = getPlayer(player)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            row = (r * -1) + (len(grid) - 1)
            if grid[row][c] == player:
                inRow = 0
                # up left
                try:
                    for i in range(4):
                        if row + i > len(grid) or c - i < 0:
                            inRow = 0
                            break
                        if grid[row + i][c - i] == player:
                            inRow += 1
                except:
                    inRow = 0
                if inRow >= 4:
                    return True
                inRow = 0
                # up right
                try:
                    for i in range(4):
                        if row + i > len(grid) or c + i > len(grid[row]):
                            inRow = 0
                            break
                        if grid[row + i][c + i] == player:
                            inRow += 1
                except:
                    inRow = 0
                if inRow >= 4:
                    return True
    return False

def checkWin(grid, player):
    if checkHorizontalWin(grid, player) or checkVerticalWin(grid, player) or checkDiagonalWin(grid, player):
        return True
    else:
        return False

def checkHorizontal(grid, player, maxGaps):
    amount = 0
    player = getPlayer(player)
    for row in grid:
        inRow = 0
        curGaps = 0
        for item in row:
            if item == player:
                inRow += 1
            elif item == "O" and curGaps < maxGaps:
                curGaps += 1
                inRow += 1
            elif item != player and inRow < 4:
                inRow = 0
        if inRow >= 4:
            amount = amount + 1
    return amount

def checkVertical(grid, player, maxGaps):
    amount = 0
    player = getPlayer(player)
    for c in range(len(grid[0])):
        inRow = 0
        curGaps = 0
        for row in range(len(grid)):
            r = (row * -1) + (len(grid) - 1)
            if grid[r][c] == player:
                inRow += 1
            elif grid[r][c] == "O" and curGaps < maxGaps:
                curGaps += 1
                inRow += 1
            elif grid[r][c] != player and inRow < 4:
                inRow = 0
        if inRow >= 4:
            amount = amount + 1
    return amount

def checkDiagonal(grid, player, maxGaps):
    amount = 0
    player = getPlayer(player)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == player:
                inRow = 0
                curGaps = 0
                # down left
                try:
                    for i in range(4):
                        if r + i > len(grid) or c - i < 0:
                            inRow = 0
                            break
                        if grid[r + i][c - i] == player:
                            inRow += 1
                        elif curGaps < maxGaps and grid[r + i][c - i] == "O":
                            curGaps += 1
                            inRow += 1
                except:
                    inRow = 0
                if inRow >= 4:
                    amount = amount + 1
                inRow = 0
                curGaps = 0
                # down right
                try:
                    for i in range(4):
                        if row + i > len(grid) or c + i > len(grid[row]):
                            inRow = 0
                            break
                        if grid[row + i][c + i] == player:
                            inRow += 1
                        elif curGaps < maxGaps and grid[row + i][c + i] == "O":
                            curGaps += 1
                            inRow += 1
                except:
                    inRow = 0
                if inRow >= 4:
                    amount = amount + 1
            row = (r * -1) + (len(grid) - 1)
            if grid[row][c] == player:
                inRow = 0
                curGaps = 0
                # up left
                try:
                    for i in range(4):
                        if row - i < 0 or c - i < 0:
                            inRow = 0
                            break
                        if grid[row - i][c - i] == player:
                            inRow += 1
                        elif curGaps < maxGaps and grid[row - i][c - i] == "O":
                            curGaps += 1
                            inRow += 1
                except:
                    inRow = 0
                if inRow >= 4:
                    amount = amount + 1
                inRow = 0
                curGaps = 0
                # up right
                try:
                    for i in range(4):
                        if row - i < 0 or c + i > len(grid[row]):
                            inRow = 0
                            break
                        if grid[row - i][c + i] == player:
                            inRow += 1
                        elif curGaps < maxGaps and grid[row - i][c + i] == "O":
                            curGaps += 1
                            inRow += 1
                except:
                    inRow = 0
                if inRow >= 4:
                    amount = amount + 1
    return amount

def check(grid, player, gaps):
    found = False
    a = 0
    a = a + checkHorizontal(grid, player, gaps)
    a = a + checkVertical(grid, player, gaps)
    a = a + checkDiagonal(grid, player, gaps)
    if a > 0:
        found = True
    return found, a
