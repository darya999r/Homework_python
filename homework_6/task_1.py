# Задача 1. Создайте программу для игры в "Крестики-нолики".

from random import randint

def board (matrix):
    row1 = row3 = row5 = row7 = '-------------'
    row2 = " ".join(map(str,matrix[0]))
    row4 = " ".join(map(str,matrix[1]))
    row6 = " ".join(map(str,matrix[2]))
    print('{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(row1,row2,row3,row4,row5,row6,row7))

def draw ():
    first_move = randint(1,2)
    return first_move

def winner (matrix):
    win_x1 = ['|','x','|','x','|','x','|']
    win_o1 = ['|','o','|','o','|','o','|']
    if matrix[0]==win_x1 or matrix[1]==win_x1 or matrix[2]==win_x1:
        win = 1
        print("The x-player won!")    
    elif matrix[0]==win_o1 or matrix[1]==win_o1 or matrix[1]==win_o1:
        win = 2
        print("The o-player won!")
    elif matrix[0][1]=='x' and matrix[1][3]=='x' and matrix[2][5]=='x':
        win = 3
        print("The x-player won!")
    elif matrix[0][1]=='o' and matrix[1][3]=='o' and matrix[2][5]=='o':
        win = 4
        print("The o-player won!")
    elif matrix[0][-2]=='x' and matrix[1][3]=='x' and matrix[2][1]=='x':
        win = 5
        print("The x-player won!")
    elif matrix[0][-2]=='o' and matrix[1][3]=='o' and matrix[2][1]=='o':
        win = 6
        print("The o-player won!")
    elif matrix[0][1]=='x' and matrix[1][1]=='x' and matrix[2][1]=='x':
        win = 7
        print("The x-player won!")
    elif matrix[0][1]=='o' and matrix[1][1]=='o' and matrix[2][1]=='o':
        win = 8
        print("The o-player won!")
    elif matrix[0][3]=='x' and matrix[1][3]=='x' and matrix[2][3]=='x':
        win = 9
        print("The x-player won!")
    elif matrix[0][3]=='o' and matrix[1][3]=='o' and matrix[2][3]=='o':
        win = 10
        print("The o-player won!")
    elif matrix[0][5]=='x' and matrix[1][5]=='x' and matrix[2][5]=='x':
        win = 11
        print("The x-player won!")
    elif matrix[0][5]=='o' and matrix[1][5]=='o' and matrix[2][5]=='o':
        win = 12
        print("The o-player won!")
    else: win = 0
    print(board(matrix))
    return win

def game_x_o (matrix,first_move):
    counter = 0
    while counter < 10:
        win = winner (matrix)
        if win == 0:
            if first_move%2!=0:
                if counter%2 == 0:
                    print("x-player move")
                    move_row = int(input("Enter row number: "))
                    move_col = int(input("Enter column number: "))
                    if move_row==1 and move_col==1:
                        if matrix[0][1]=='x' or matrix[0][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][1]='x'
                    elif move_row==1 and move_col==2:
                        if matrix[0][3]=='x' or matrix[0][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][3]='x'
                    elif move_row==1 and move_col==3:
                        if matrix[0][5]=='x' or matrix[0][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][5]='x'
                    elif move_row==2 and move_col==1:
                        if matrix[1][1]=='x' or matrix[1][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][1]='x'
                    elif move_row==2 and move_col==2:
                        if matrix[1][3]=='x' or matrix[1][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][3]='x'
                    elif move_row==2 and move_col==3:
                        if matrix[1][5]=='x' or matrix[1][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][5]='x'
                    elif move_row==3 and move_col==1:
                        if matrix[2][1]=='x' or matrix[2][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][1]='x'
                    elif move_row==3 and move_col==2:
                        if matrix[2][3]=='x' or matrix[2][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][3]='x'
                    elif move_row==3 and move_col==3:
                        if matrix[2][5]=='x' or matrix[2][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][5]='x'
                    counter += 1

                elif counter%2 != 0:
                    print("o-player move")
                    move_row = int(input("Enter row number: "))
                    move_col = int(input("Enter column number: "))
                    if move_row==1 and move_col==1:
                        if matrix[0][1]=='x' or matrix[0][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][1]='o'
                    elif move_row==1 and move_col==2:
                        if matrix[0][3]=='x' or matrix[0][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][3]='o'
                    elif move_row==1 and move_col==3:
                        if matrix[0][5]=='x' or matrix[0][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][5]='o'
                    elif move_row==2 and move_col==1:
                        if matrix[1][1]=='x' or matrix[1][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][1]='o'
                    elif move_row==2 and move_col==2:
                        if matrix[1][3]=='x' or matrix[1][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][3]='o'
                    elif move_row==2 and move_col==3:
                        if matrix[1][5]=='x' or matrix[1][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][5]='o'
                    elif move_row==3 and move_col==1:
                        if matrix[2][1]=='x' or matrix[2][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][1]='o'
                    elif move_row==3 and move_col==2:
                        if matrix[2][3]=='x' or matrix[2][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][3]='o'
                    elif move_row==3 and move_col==3:
                        if matrix[2][5]=='x' or matrix[2][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][5]='o'
                    counter += 1

            else:    
                if counter%2 == 0:
                    print("o-player move")
                    move_row = int(input("Enter row number: "))
                    move_col = int(input("Enter column number: "))
                    if move_row==1 and move_col==1:
                        if matrix[0][1]=='x' or matrix[0][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][1]='o'
                    elif move_row==1 and move_col==2:
                        if matrix[0][3]=='x' or matrix[0][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][3]='o'
                    elif move_row==1 and move_col==3:
                        if matrix[0][5]=='x' or matrix[0][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][5]='o'
                    elif move_row==2 and move_col==1:
                        if matrix[1][1]=='x' or matrix[1][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][1]='o'
                    elif move_row==2 and move_col==2:
                        if matrix[1][3]=='x' or matrix[1][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][3]='o'
                    elif move_row==2 and move_col==3:
                        if matrix[1][5]=='x' or matrix[1][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][5]='o'
                    elif move_row==3 and move_col==1:
                        if matrix[2][1]=='x' or matrix[2][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][1]='o'
                    elif move_row==3 and move_col==2:
                        if matrix[2][3]=='x' or matrix[2][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][3]='o'
                    elif move_row==3 and move_col==3:
                        if matrix[2][5]=='x' or matrix[2][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][5]='o'
                    counter += 1

                elif counter%2 != 0:
                    print("x-player move")
                    move_row = int(input("Enter row number: "))
                    move_col = int(input("Enter column number: "))
                    if move_row==1 and move_col==1:
                        if matrix[0][1]=='x' or matrix[0][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][1]='x'
                    elif move_row==1 and move_col==2:
                        if matrix[0][3]=='x' or matrix[0][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][3]='x'
                    elif move_row==1 and move_col==3:
                        if matrix[0][5]=='x' or matrix[0][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[0][5]='x'
                    elif move_row==2 and move_col==1:
                        if matrix[1][1]=='x' or matrix[1][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][1]='x'
                    elif move_row==2 and move_col==2:
                        if matrix[1][3]=='x' or matrix[1][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][3]='x'
                    elif move_row==2 and move_col==3:
                        if matrix[1][5]=='x' or matrix[1][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[1][5]='x'
                    elif move_row==3 and move_col==1:
                        if matrix[2][1]=='x' or matrix[2][1]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][1]='x'
                    elif move_row==3 and move_col==2:
                        if matrix[2][3]=='x' or matrix[2][3]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][3]='x'
                    elif move_row==3 and move_col==3:
                        if matrix[2][5]=='x' or matrix[2][5]=='o':
                            print("The cage is occupied! Make a different move!")
                            counter -= 1
                        else: matrix[2][5]='x'
                    counter += 1

        else: 
            break
    else: 
        print("Nobody won!")
         


row2 = ['|',' ','|',' ','|',' ','|']
row4 = ['|',' ','|',' ','|',' ','|']
row6 = ['|',' ','|',' ','|',' ','|']
matrix = [row2,row4,row6]

first_move = draw()
print("1 plaer = 'x', 2 plaer = 'o'.\nFirst move: ", first_move)

game_x_o (matrix,first_move)

