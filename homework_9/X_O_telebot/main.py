import telebot
from telebot import types
import logger
import bot_ai


API_TOKEN='tokentokentoken'
bot = telebot.TeleBot(API_TOKEN)

start_game = False

person_mark = "x"
bot_mark = "o"

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

print('bot is start')

def winnerPerson() -> bool:
    global board
    global win
    for move in win:
        if board[move[0]]==board[move[1]]==board[move[2]]=="x":
            return True


def winnerBot() -> bool:
    global board
    global win
    for move in win:
        if board[move[0]]==board[move[1]]==board[move[2]]=="o":
            return True


def draw() -> bool:
    global board
    global win
    draw_board = "".join(map(str,board))
    if draw_board.isalpha():
        for move in win:
            if board[move[0]]=='x' and board[move[1]]==board[move[2]]=='o':
                return True
            elif board[move[0]]=='o' and board[move[1]]==board[move[2]]=='x':
                return True
            elif board[move[1]]=='x' and board[move[0]]==board[move[2]]=='o':
                return True
            elif board[move[1]]=='o' and board[move[0]]==board[move[2]]=='x':
                return True

def clear():
    global board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

@bot.message_handler(commands=['start'])
def startMessage(message):
    key = {}
    keyboard_1 = types.ReplyKeyboardMarkup(True, True)
    key[0] = types.KeyboardButton("Список прошедших игр")
    key[1] = types.KeyboardButton("Очистить список игр")
    key[2] = types.KeyboardButton("Новая игра х-о")
    keyboard_1.add(key[0], key[1], key[2])

    name = message.from_user.first_name
    bot.send_message(message.chat.id,f"Привет, {name}!\nЯ хо-хо-хо-бот и я очень люблю играть в крестики-нолики!Сразись со мной ;)\nЧтобы начать игру нажми 'Новая игра х-о'", parse_mode='html', reply_markup=keyboard_1)
    return name

@bot.message_handler(content_types=['text'])
def main(message):
    global start_game
    if message.chat.type == 'private':
        if message.text == "Список прошедших игр":
            log_print = logger.view_log()
            bot.send_message(message.chat.id, log_print)
        elif message.text == "Очистить список игр":
            logger.clear_log()
            bot.send_message(message.chat.id,"Список игр очищен.")
        elif message.text == "Новая игра х-о":
            start_game = True
        else:
            bot.send_message(message.chat.id, "Я не знаю таких слов :(")
    
    if start_game == True:
        global board
        bot.send_message(message.chat.id, "Игра началась")
        markup = types.InlineKeyboardMarkup(row_width=3)
        cage = {}
        i = 0
        for i in range(9):
            cage[i] = types.InlineKeyboardButton(text = board[i], callback_data=str(i))
        markup.row(cage[0], cage[1], cage[2])
        markup.row(cage[3], cage[4], cage[5])
        markup.row(cage[6], cage[7], cage[8])
        bot.send_message(chat_id=message.chat.id, text="Выбери клетку", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    global board
    global start_game
    global win
    cage = {}
    name = call.from_user.first_name

    if call.message:
        # person move:
        i=0
        for i in range(9):
            if call.data == str(i):
                if board[i] == " ":
                    board[i] = person_mark
                    cage[i] = types.InlineKeyboardButton(text = person_mark, callback_data=str(i))
        
        if winnerPerson():
            bot.send_message(call.message.chat.id, "Я проиграл :(")
            start_game = False
            clear()
            who_win = 'победил игрок'
            logger.datetime(name,who_win)
        if draw():
            bot.send_message(call.message.chat.id, "Ничья! Давай сыграем ещё раз!\nВыбери в Menu команду /start")
            start_game = False
            clear()
            who_win = 'ничья'
            logger.datetime(name,who_win)
        if start_game:
            markup = types.InlineKeyboardMarkup(row_width=3)
            i = 0
            for i in range(9):
                cage[i] = types.InlineKeyboardButton(text = board[i], callback_data=str(i))
            markup.row(cage[0], cage[1], cage[2])
            markup.row(cage[3], cage[4], cage[5])
            markup.row(cage[6], cage[7], cage[8])
            bot.send_message(chat_id=call.message.chat.id, text="Твой ход", reply_markup=markup)

            # bot move:
            board = bot_ai.botMove(board, win)

            if winnerBot():
                bot.send_message(call.message.chat.id, "Я выиграл ;)")
                start_game = False
                clear()
                who_win = 'победил бот'
                logger.datetime(name,who_win)
            if draw():
                bot.send_message(call.message.chat.id, "Ничья! Попробуй ещё раз! :P")
                start_game = False
                clear()
                who_win = 'ничья'
                logger.datetime(name,who_win)

        if start_game:
            markup = types.InlineKeyboardMarkup(row_width=3)
            i = 0
            for i in range(9):
                cage[i] = types.InlineKeyboardButton(text = board[i], callback_data=str(i))
            markup.row(cage[0], cage[1], cage[2])
            markup.row(cage[3], cage[4], cage[5])
            markup.row(cage[6], cage[7], cage[8])
            bot.send_message(chat_id=call.message.chat.id, text="Я походил. Твоя очередь:", reply_markup=markup)
        
        
bot.polling(none_stop=True)        
            