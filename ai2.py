import random, grids, copy, checker

maxDepth = 0

def play(grid, depth):
    global maxDepth
    maxDepth = depth
    curDepth = 0
    tempGrid = copy.deepcopy(grid)
    scores = getMaxFirst(tempGrid, curDepth)
    for i in range(len(scores)):
        tempGrid = copy.deepcopy(grid)
        tempGrid, valid = grids.addValid(scores[i][1], 0, tempGrid)
        if valid:
            break
    return tempGrid

    
def score(grid, col):
    s = 0
    found, amount = checker.check(grid, 0, 2)
    if found:
        for i in range(amount):
            s = s + 3
    found, amount = checker.check(grid, 0, 1)
    if found:
        for i in range(amount):
            s = s + 5
    found, amount = checker.check(grid, 1, 2)
    if found:
        for i in range(amount):
            s = s - 2
    found, amount = checker.check(grid, 1, 1)
    if found:
        for i in range(amount):
            s = s - 3
            
    if checker.checkWin(grid, 0):
        s = s + 1000

    if checker.checkWin(grid, 1):
        s = s - 100
        
    if col == 4:
        s = s + 4
    return s

def getMaxFirst(grid, curDepth):
    global maxDepth
    curDepth += 1
    scores = []
    if curDepth == maxDepth:
        for i in range(1,len(grid[0]) + 1):
            tempGrid = copy.deepcopy(grid)
            tempGrid = grids.add(i, 0, tempGrid)
            s = score(tempGrid, i)
            scores.append([s, i])
    else:
        for i in range(1,len(grid[0]) + 1):
            tempGrid = copy.deepcopy(grid)
            tempGrid = grids.add(i, 0, tempGrid)
            s, column = getMin(tempGrid, curDepth)
            scores.append([s, i])
    scores = sorted(scores, reverse = True, key=lambda x:x[0])
    return scores

def getMax(grid, curDepth):
    global maxDepth
    curDepth += 1
    scores = []
    won = checker.checkWin(grid, 0)
    if won:
        return 1000, 0
    elif curDepth == maxDepth:
        for i in range(1,len(grid[0]) + 1):
            tempGrid = copy.deepcopy(grid)
            tempGrid = grids.add(i, 0, tempGrid)
            s = score(tempGrid, i)
            scores.append([s, i])
    else:
        for i in range(1,len(grid[0]) + 1):
            tempGrid = copy.deepcopy(grid)
            tempGrid = grids.add(i, 0, tempGrid)
            s, column = getMin(tempGrid, curDepth)
            scores.append([s, i])
    scores = sorted(scores, reverse = True, key=lambda x:x[0])
    return scores[0][0], scores[0][1]

def getMin(grid, curDepth):
    global maxDepth
    curDepth += 1
    scores = []
    won = checker.checkWin(grid, 1)
    if won:
        return -100, 0
    elif curDepth == maxDepth:
        for i in range(1,len(grid[0]) + 1):
            tempGrid = copy.deepcopy(grid)
            tempGrid = grids.add(i, 1, tempGrid)
            s = score(tempGrid, i)
            scores.append([s, i])
    else:
        for i in range(1,len(grid[0]) + 1):
            tempGrid = copy.deepcopy(grid)
            tempGrid = grids.add(i, 1, tempGrid)
            s, column = getMax(tempGrid, curDepth)
            scores.append([s, i])
    scores = sorted(scores, key=lambda x:x[0])
    return scores[0][0], scores[0][1]
