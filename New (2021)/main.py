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
                    print(f"Horizontal Win {player}")
                    return True
            
        # Vertical
        for i in range(7):
            for j in range(3):
                if sum([self.grid[x + i] for x in range (j * 7, (j + 4) * 7, 7)]) == 4 * player:
                    print(f"Vertical Win {player}")
                    return True

        # Diagonal UP RIGHT

        # Diagonal DOWN RIGHT

        return False

    def printGrid(self):
        print("-----------------------")
        for i in range(5, -1, -1):
            row = "|"
            for j in range(7):
                row += f" {self.grid[(i * 7) + j]} "
            print(row + "|")
        print("-----------------------")

g = Grid()
g.printGrid()

while True:
    col = int(input("Column: "))
    g.makeMove(col, 1)
    g.printGrid()
    g.checkWin(1)