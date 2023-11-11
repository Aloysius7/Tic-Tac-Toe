count = 1
X = ' X |'
O = ' O |'
grid = [
    ['   |', '   |', '  '],
    ['-----------'],
    ['   |', '   |', '  '],
    ['-----------'],
    ['   |', '   |', '  '],
]
Playable = True
Input_is_Correct = True


def welcome_msg(original_grid):
    display_grid = [row[:] for row in original_grid]
    print("Welcome to the game of TIC TAC TOE\n")
    display_grid[0][0] = ' 0 |'
    display_grid[0][1] = ' 1 |'
    display_grid[0][2] = ' 2 '
    display_grid[2][0] = ' 3 |'
    display_grid[2][1] = ' 4 |'
    display_grid[2][2] = ' 5 '
    display_grid[4][0] = ' 6 |'
    display_grid[4][1] = ' 7 |'
    display_grid[4][2] = ' 8 '

    for row in display_grid:
        print(''.join(row))
    print("\n\n")


def edit_grid(editted_grid):
    global count, grid, X, O, Playable, Input_is_Correct
    try:
        while Input_is_Correct:
            if Playable:
                row = int(input("Choose Row (1-3): "))
                column = int(input("Choose Column (1-3): "))

                if row > 3 or row < 0 or column > 3 or column < 0:
                    print('You have entered a out of range index, Enter Again!!!!')
                else:
                    if count % 2 == 0:
                        if column == 3:
                            move = ' O '
                        else:
                            move = ' O |'
                    else:
                        if column == 3:
                            move = ' X '
                        else:
                            move = ' X |'

                    editted_grid[row - 1][column - 1] = move
                    editted_grid.insert(1, grid[1])
                    editted_grid.insert(3, grid[3])
                    for row in editted_grid:
                        print(''.join(row))
                    print("\n\n")
                    count += 1
                    editted_grid.remove(grid[1])
                    editted_grid.remove(grid[3])
                    check_winner(editted_grid)
    except:
        print("Enter Valid Input, No alphabets allowed.")


def check_winner(main_grid):
    global Input_is_Correct
    if count < 9:
        # Check Rows
        for row in main_grid:
            r = ''.join(row)
            rO = sum(1 for char in r if char == 'O')
            rx = sum(1 for char in r if char == 'X')
            if rO == 3:
                print('O won')
                Input_is_Correct = False
            elif rx == 3:
                print('X won')
                Input_is_Correct = False

        # Check Columns
        for i in range(3):
            c = "".join(main_grid[j][i] for j in range(3))
            rO = sum(1 for char in c if char == 'O')
            rx = sum(1 for char in c if char == 'X')
            if rO == 3:
                print('O won')
                Input_is_Correct = False
            elif rx == 3:
                print('X won')
                Input_is_Correct = False

        # Check Diagonals
        d1 = main_grid[0][0] + main_grid[1][1] + main_grid[2][2]
        d2 = main_grid[0][2] + main_grid[1][1] + main_grid[2][0]
        rO = sum(1 for char in d1 or d2 if char == 'O')
        rx = sum(1 for char in d1 or d2 if char == 'X')
        if rO == 3:
            print('O won')
            Input_is_Correct = False
        elif rx == 3:
            print('X won')
            Input_is_Correct = False
    else:
        Input_is_Correct = False
        print("Draw")


welcome_msg(grid)
new_grid = [row[:] for row in grid[::2]]
while count <= 9 and Playable:
    edit_grid(new_grid)
