import pygame, math, copy, os

class Grid:
    def __init__(self, grid = [0]*42):
        self.grid = grid

    def makeMove(self, column, player):
        for i in [ x + column for x in range(0, 42, 7) ]:
            if self.grid[i] == 0:
                self.grid[i] = player
                return True
        return False

    def getMove(self, column, player):
        new_grid = copy.copy(self.grid)
        for i in [ x + column for x in range(0, 42, 7) ]:
            if new_grid[i] == 0:
                new_grid[i] = player
                return new_grid

    def checkWin(self, player):
        # Horizontal
        for i in range(6):
            for j in range(4):
                if sum(self.grid[i * 7 + j:i * 7 + j + 4]) == 4 * player:
                    return True
            
        # Vertical
        for i in range(7):
            for j in range(3):
                if sum([self.grid[x + i] for x in range (j * 7, (j + 4) * 7, 7)]) == 4 * player:
                    return True

        # Diagonal UP RIGHT
        for i in range(4):
            for j in range(3):
                if sum([ self.grid[i + (7 * j) + r] for r in range(0, 25, 8) ]) == 4 * player:
                    return True

        # Diagonal DOWN RIGHT
        for i in range(3,7):
            for j in range(3):
                if sum([ self.grid[i + (7 * j) + r] for r in range(0, 19, 6) ]) == 4 * player:
                    return True
        return False

    def returnLineAmounts(self, score, player):

        amount = 0

        # Horizontal
        for i in range(6):
            for j in range(4):
                if sum(self.grid[i * 7 + j:i * 7 + j + 4]) == score * player:
                    amount += 1
        # Vertical
        for i in range(7):
            for j in range(3):
                if sum([self.grid[x + i] for x in range (j * 7, (j + 4) * 7, 7)]) == score * player:
                    amount += 1
        # Diagonal UP RIGHT
        for i in range(4):
            for j in range(3):
                if sum([ self.grid[i + (7 * j) + r] for r in range(0, 25, 8) ]) == score * player:
                    amount += 1
        # Diagonal DOWN RIGHT
        for i in range(3,7):
            for j in range(3):
                if sum([ self.grid[i + (7 * j) + r] for r in range(0, 19, 6) ]) == score * player:
                    amount += 1

        return amount

    def generateGrids(self, player):
        grids = []
        columnOrder = [3, 2, 4, 1, 5, 0, 6]
        for column in columnOrder:
            if self.grid[column + 35] == 0:
                grids.append((column, Grid(self.getMove(column, player))))
        return grids

    def calculateScore(self):

        score = 0

        if self.checkWin(1):
            score += math.inf

        if self.checkWin(-1):
            score -= math.inf

        score += self.returnLineAmounts(3, 1) * 5
        score += self.returnLineAmounts(2, 1) * 2
        score -= self.returnLineAmounts(3, -1) * 5
        score -= self.returnLineAmounts(2, -1) * 2

        return score

    def printGrid(self):
        symbols = {0:' ', 1:'O', -1: 'X'}
        print("-----------------------")
        for i in range(5, -1, -1):
            row = "|"
            for j in range(7):
                row += f"|{symbols[self.grid[(i * 7) + j]]}|"
            print(row + "|")
        print("-----------------------")

def minimax(grid, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or grid.checkWin(-1) or grid.checkWin(1):
        return grid.calculateScore(), (0, 0)
    if maximizingPlayer:
        value = -math.inf
        bestMove = None
        for move, result in grid.generateGrids(1):
            old_value = value
            value = max(value, minimax(result, depth - 1, alpha, beta, False)[0])
            if old_value != value:
                bestMove = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
    else:
        value = math.inf
        bestMove = None
        for move, result in grid.generateGrids(-1):
            old_value = value
            value = min(value, minimax(result, depth - 1, alpha, beta, True)[0])
            if old_value != value:
                bestMove = move
            beta = min(beta, value)
            if beta <= alpha:
                break
    return value, bestMove

g = Grid()
g.printGrid()

player = 1

depth = 6

while True:
    col = int(input("Column: "))
    g.makeMove(col, player)
    
    if g.checkWin(1):
        g.printGrid()
        break

    g.makeMove(minimax(g, depth, -math.inf, math.inf, -player == 1)[1], -player)
    
    if g.checkWin(-1):
        g.printGrid()
        break

    g.printGrid()