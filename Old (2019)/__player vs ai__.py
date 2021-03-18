import grids, ai, copy, checker, turtle

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
        turtle.write("You Win!",False,align="center",font=("Courier New",72,"bold"))
    elif winner == 2:
        turtle.write("You Lose!",False,align="center",font=("Courier New",72,"bold"))

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

def difficulty():
    print("What difficulty of ai would you like to play against?")
    print("1 - easy")
    print("2 - normal")
    print("3 - hard")
    print("4 - expert")
    print("(as difficulty increases, so does the time it takes for")
    print("the ai to make its move)")
    while True:
        try:
            while True:
                choice = int(input("Enter the number of your choice: "))
                if choice < 1 or choice > 4:
                    print("That is not a valid difficulty!")
                else:
                    break
            break
        except:
            print("That is not a valid difficulty!")
    if choice == 3:
        choice = 4
    elif choice == 4:
        choice = 5
    return choice

while True:
    grid = grids.reset()
    depth = difficulty()
    playing = True
    winner = 0
    while playing:
        print(grids.print(grid))
        printGrid(grid, 3)
        grid = player(grid)
        if checker.checkWin(grid, 0):
            winner = 1
            playing = False
            break
        elif checker.checkDraw(grid):
            playing = False
        printGrid(grid, 3)
        grid = ai.play(grid, depth)
        if checker.checkWin(grid, 1):
            winner = 2
            playing = False
            break
        elif checker.checkDraw(grid):
            playing = False

    print(grids.print(grid))
    if winner == 0:
        print("Unlucky! It was a draw!")
    elif winner == 1:
        print("You won! Well done!")
    elif winner == 2:
        print("Unlucky! You lost this one!")
    printGrid(grid, winner)
    if input("Would you like to play again? (y/n): ") == "y":
        print("\nReloading...\n\n\n")
    else:
        print("\nOkay! Shutting down...")
        break
