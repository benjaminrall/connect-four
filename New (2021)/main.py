import pygame, math, copy, os

pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 800
ICON_IMG = pygame.image.load(os.path.join("imgs","icon.png"))
GRID_IMG = pygame.image.load(os.path.join("imgs","grid.png"))
COLOURS = {0: (255, 255, 255), 1: (255, 0, 0), -1: (255, 255, 0)}
FONT = pygame.font.SysFont("georgia", 50)

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

    def checkDraw(self):
        for pos in self.grid:
            if pos == 0:
                return False
        return True

    def displayGrid(self, win):
        y_values = [400, 320, 240, 160, 80, 0]
        for i in range(7):
            for j in range(6):
                pygame.draw.rect(win, COLOURS[self.grid[i + (7 * j)]], (i * 90, y_values[j], 90, 80))

def minimax(grid, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or grid.checkWin(-1) or grid.checkWin(1):
        return grid.calculateScore(), -1
    if maximizingPlayer:
        value = -math.inf
        bestMove = None
        grids = grid.generateGrids(1)
        for move, result in grids:
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
        grids = grid.generateGrids(-1)
        for move, result in grids:
            old_value = value
            value = min(value, minimax(result, depth - 1, alpha, beta, True)[0])
            if old_value != value:
                bestMove = move
            beta = min(beta, value)
            if beta <= alpha:
                break
    return value, bestMove

def drawGame(screen, win, grid, won, winner):
    screen.fill([255, 255, 255])
    grid.displayGrid(win)
    screen.blit(win, (85, 160))
    screen.blit(GRID_IMG, (80, 150))
    if won:
        win_text = FONT.render(winner, 1, (0, 0, 0))
        restart_text = FONT.render("Press 'R' to restart.", 1, (0, 0, 0))
        screen.blit(win_text, (400 - (win_text.get_width() // 2), 10))
        screen.blit(restart_text, (400 - (restart_text.get_width() // 2), 800 - 30 - restart_text.get_height()))
    pygame.display.update()

pygame.display.set_caption("Connect 4")
pygame.display.set_icon(ICON_IMG)
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
win = pygame.Surface((630, 480))

clock = pygame.time.Clock()

g = Grid()

turn = 1
winner = 0
player = 1

depth = int(input("Enter depth: "))

run = True
playing = True

while run:
    clock.tick(60)
    
    if g.checkWin(player) and playing:
        winner = "Player wins!"
        playing = False
    if g.checkWin(-player) and playing:
        winner = "Computer wins!"
        playing = False
    if g.checkDraw() and playing:
        winner = "Draw!"
        playing = False

    if turn == -player:
        g.makeMove(minimax(g, depth, -math.inf, math.inf, -player == 1)[1], -player)
        turn = player

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and turn == player and playing:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 85 and pos[0] <= 715 and pos[1] >= 160 and pos[1] <= 640:
                    if g.makeMove((pos[0] - 85) // 90, player):
                        turn = -player

        elif event.type == pygame.KEYDOWN and not playing:
            if event.key == pygame.K_r:
                player = -player
                turn = player
                g = Grid([0]*42)
                if player != 1:
                    g.makeMove(3, -player)
                playing = True

    drawGame(screen, win, g, not playing, winner)