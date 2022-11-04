import random

def botMove(board, win):
    bot_mark = "o"
    move = random.randint(0,8)
    if board[4] == " ":
        board[4] = bot_mark
        return board
    for pos in win:
        if board[pos[0]]==board[pos[1]]=="o" and board[pos[2]]==" ":
            board[pos[2]]=bot_mark
            return board
        elif board[pos[0]]==board[pos[2]]=="o" and board[pos[1]]==" ":
            board[pos[1]]=bot_mark
            return board
        elif board[pos[1]]==board[pos[2]]=="o" and board[pos[0]]==" ":
            board[pos[0]]=bot_mark
            return board
    for pos in win:
        if board[pos[0]]==board[pos[1]]=="x" and board[pos[2]]==" ":
            board[pos[2]]=bot_mark
            return board
        elif board[pos[0]]==board[pos[2]]=="x" and board[pos[1]]==" ":
            board[pos[1]]=bot_mark
            return board
        elif board[pos[1]]==board[pos[2]]=="x" and board[pos[0]]==" ":
            board[pos[0]]=bot_mark
            return board
    if board[move]==" ":
            board[move]=bot_mark
            return board