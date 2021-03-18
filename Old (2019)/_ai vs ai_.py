import grids, ai, copy, checker, turtle, ai2

print("""---------- WELCOME TO CONNECT 4 ----------
In this game, the aim is to have 4 of your
counters in a single row. Each round, you
may place your counter in any column you
desire and then the computer will make its
move. Try to outsmart the computer and win!\n""")
print("""Key:
'O' = unoccupied space
'P' = player occupied space
'C' = computer occupied space\n\n""")

def printGrid(grid, winner):
    turtle.reset()
    turtle.speed("fastest")
    turtle.fillcolor("blue")
    turtle.speed(0)
    turtle.ht()
    turtle.pu()
    turtle.setx(-350)
    turtle.sety(350)
    turtle.pd()
    turtle.begin_fill()
    turtle.fd(700)
    turtle.right(90)
    turtle.fd(620)
    turtle.right(90)
    turtle.fd(700)
    turtle.right(90)
    turtle.fd(620)
    turtle.right(90)
    turtle.end_fill()
    turtle.tracer(0,0)
    for row in grid:
        turtle.pu()
        turtle.right(90)
        turtle.fd(120)
        turtle.left(90)
        turtle.fd(50)
        turtle.left(90)
        turtle.fd(20)
        turtle.right(90)
        turtle.pd()
        for item in row:
            if item == "O":
                turtle.fillcolor("white")
            elif item == "P":
                turtle.fillcolor("yellow")
            else:
                turtle.fillcolor("red")
            turtle.begin_fill()
            turtle.circle(40)
            turtle.end_fill()
            turtle.pu()
            turtle.fd(100)
        turtle.right(180)
        turtle.fd(750)
        turtle.right(180)
    turtle.update()
    turtle.home()
    turtle.sety(-400)
    turtle.pd()
    if winner == 0:
        turtle.write("Draw!",False,align="center",font=("Courier New",72,"bold"))
    elif winner == 1:
        turtle.write("Yellow Wins!",False,align="center",font=("Courier New",72,"bold"))
    elif winner == 2:
        turtle.write("Red Wins!",False,align="center",font=("Courier New",72,"bold"))

def player(grid):
    while True:
        while True:
            try:
                while True:
                    column = int(input("Enter a column (1-7): "))
                    if column < 1 or column > 7:
                        print("That is not a valid column!")
                    else:
                        break
                break
            except:
                print("That is not a valid column!")
    
        grid, valid = grids.addValid(column, 0, grid)
        if valid:
            break
        else:
            print("Not valid - column full!")
    return grid

while True:
    grid = grids.reset()
    playing = True
    winner = 0
    depth1 = int(input("Enter depth for yellow: "))
    depth2 = int(input("Enter depth for red: "))
    while playing:
        print(grids.print(grid))
        printGrid(grid, 3)
        grid = ai2.play(grid, depth1)
        if checker.checkWin(grid, 0):
            winner = 1
            playing = False
            break
        elif checker.checkDraw(grid):
            playing = False
        print(grids.print(grid))
        printGrid(grid, 3)
        grid = ai.play(grid, depth2)
        if checker.checkWin(grid, 1):
            winner = 2
            playing = False
            break
        elif checker.checkDraw(grid):
            playing = False

    print(grids.print(grid))
    if winner == 0:
        print("It was a draw!")
    elif winner == 1:
        print("Yellow AI won!")
    elif winner == 2:
        print("Red AI won!")
    printGrid(grid, winner)
    if input("Would you like them to battle again? (y/n): ") == "y":
        print("\nReloading...\n\n\n")
    else:
        print("\nOkay! Shutting down...")
        break
