# Задача FOOTBALL необязательная: 
# Напишите программу, которая принимает на стандартный вход 
# список игр футбольных команд с результатом матча и 
# выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

# ТОЛЬКО ДЛЯ 3х КОММАНД!

def enter_game():
    list_g = []
    list_g.append(input("Enter the name of the first team: "))
    list_g.append(int(input("Enter the number of goals scored: ")))
    list_g.append(input("Enter the name of the second team: "))
    list_g.append(int(input("Enter the number of goals scored: ")))
    return list_g

def save_games(nn):
    n = nn
    list_games = []
    while n!=0:
        list_g = enter_game()
        list_games.append(list_g)
        n -= 1
    with open ('games.txt', 'w', encoding="utf-8") as file:
            file.write(str(list_games))
    return list_games
    
def print_games(nn, list_1):
    print("\nNumber of games: ", nn)
    print()
    print("1 command:           Goals:                   2 command:           Goals:")
    for i in range(len(list_1)):
            print('{:<22} {:<22} {:<22} {:<22}\n'.format(list_1[i][0],list_1[i][1],list_1[i][2],list_1[i][3]))
        
def info_commands(nn, list_2):
    info_1 = []
    info_2 = []
    info_3 = []
    champ_1 = 0
    champ_2 = 0
    champ_3 = 0
    draw_1 = 0
    draw_2 = 0
    draw_3 = 0
    loss_1 = 0
    loss_2 = 0
    loss_3 = 0
    point_1 = 0
    point_2 = 0
    point_3 = 0
    
    if nn==3:
        com_1 = list_2[0][0]
        com_2 = list_2[0][2]
        if com_1!=list_2[1][0] and com_2!=list_2[1][0]:
            com_3 = list_2[1][0]
        else:
            com_3 = list_2[1][2]
        info_1.append(com_1)
        info_2.append(com_2)
        info_3.append(com_3)
        info_1.append(nn-1)
        info_2.append(nn-1)
        info_3.append(nn-1)
        if list_2[0][1]>list_2[0][3]:
            champ_1 += 1
            point_1 += 3
            loss_2 += 1
        elif list_2[0][1]<list_2[0][3]:
            champ_2 += 1
            point_2 += 3
            loss_1 += 1
        elif list_2[0][1]==list_2[0][3]:
            draw_1 += 1
            point_1 += 1
            draw_2 += 1
            point_2 += 1
        if list_2[1][1]>list_2[1][3]:
            if list_2[1][0]==com_3 and list_2[1][2]==com_1:
                champ_3 += 1
                point_3 += 3
                loss_1 += 1
            elif list_2[1][0]==com_3 and list_2[1][2]==com_2:
                champ_3 += 1
                point_3 += 3
                loss_2 += 1
            elif list_2[1][0]==com_2 and list_2[1][2]==com_1:
                champ_2 += 1
                point_2 += 3
                loss_1 += 1
            elif list_2[1][0]==com_2 and list_2[1][2]==com_3:
                champ_2 += 1
                point_2 += 3
                loss_3 += 1
            elif list_2[1][0]==com_1 and list_2[1][2]==com_3:
                champ_1 += 1
                point_1 += 3
                loss_3 += 1
            elif list_2[1][0]==com_1 and list_2[1][2]==com_2:
                champ_1 += 1
                point_1 += 3
                loss_2 += 1
        elif list_2[1][1]<list_2[1][3]:
            if list_2[1][0]==com_3 and list_2[1][2]==com_1:
                loss_3 += 1
                champ_1 += 1
                point_1 += 3
            elif list_2[1][0]==com_3 and list_2[1][2]==com_2:
                loss_3 += 1
                champ_2 += 1
                point_2 += 3
            elif list_2[1][0]==com_2 and list_2[1][2]==com_1:
                loss_2 += 1
                champ_1 += 1
                point_1 += 3
            elif list_2[1][0]==com_2 and list_2[1][2]==com_3:
                loss_2 += 1
                champ_3 += 1
                point_3 += 3
            elif list_2[1][0]==com_1 and list_2[1][2]==com_3:
                loss_1 += 1
                champ_3 += 1
                point_3 += 3
            elif list_2[1][0]==com_1 and list_2[1][2]==com_2:
                loss_1 += 1
                champ_2 += 1
                point_2 += 3
        elif list_2[1][1]==list_2[1][3]:
            if (list_2[1][0]==com_3 or list_2[1][2]==com_1) and (list_2[1][0]==com_1 or list_2[1][2]==com_3):
                draw_1 += 1
                point_1 += 1
                draw_3 += 1
                point_3 += 1
            elif (list_2[1][0]==com_3 or list_2[1][2]==com_2) and (list_2[1][0]==com_2 or list_2[1][2]==com_3):
                draw_2 += 1
                point_2 += 1
                draw_3 += 1
                point_3 += 1
            elif (list_2[1][0]==com_2 or list_2[1][2]==com_1) and (list_2[1][0]==com_1 or list_2[1][2]==com_2):
                draw_1 += 1
                point_1 += 1
                draw_2 += 1
                point_2 += 1
        if list_2[2][1]>list_2[2][3]:
            if list_2[2][0]==com_3 and list_2[2][2]==com_1:
                champ_3 += 1
                point_3 += 3
                loss_1 += 1
            elif list_2[2][0]==com_3 and list_2[2][2]==com_2:
                champ_3 += 1
                point_3 += 3
                loss_2 += 1
            elif list_2[2][0]==com_2 and list_2[2][2]==com_1:
                champ_2 += 1
                point_2 += 3
                loss_1 += 1
            elif list_2[2][0]==com_2 and list_2[2][2]==com_3:
                champ_2 += 1
                point_2 += 3
                loss_3 += 1
            elif list_2[2][0]==com_1 and list_2[2][2]==com_3:
                champ_1 += 1
                point_1 += 3
                loss_3 += 1
            elif list_2[2][0]==com_1 and list_2[2][2]==com_2:
                champ_1 += 1
                point_1 += 3
                loss_2 += 1
        elif list_2[2][1]<list_2[2][3]:
            if list_2[2][0]==com_3 and list_2[2][2]==com_1:
                loss_3 += 1
                champ_1 += 1
                point_1 += 3
            elif list_2[2][0]==com_3 and list_2[2][2]==com_2:
                loss_3 += 1
                champ_2 += 1
                point_2 += 3
            elif list_2[2][0]==com_2 and list_2[2][2]==com_1:
                loss_2 += 1
                champ_1 += 1
                point_1 += 3
            elif list_2[2][0]==com_2 and list_2[2][2]==com_3:
                loss_2 += 1
                champ_3 += 1
                point_3 += 3
            elif list_2[2][0]==com_1 and list_2[2][2]==com_3:
                loss_1 += 1
                champ_3 += 1
                point_3 += 3
            elif list_2[2][0]==com_1 and list_2[2][2]==com_2:
                loss_1 += 1
                champ_2 += 1
                point_2 += 3
        elif list_2[2][1]==list_2[2][3]:
            if (list_2[2][0]==com_3 or list_2[2][2]==com_1) and (list_2[2][0]==com_1 or list_2[2][2]==com_3):
                draw_1 += 1
                point_1 += 1
                draw_3 += 1
                point_3 += 1
            elif (list_2[2][0]==com_3 or list_2[2][2]==com_2) and (list_2[2][0]==com_2 or list_2[2][2]==com_3):
                draw_2 += 1
                point_2 += 1
                draw_3 += 1
                point_3 += 1
            elif (list_2[2][0]==com_2 or list_2[2][2]==com_1) and (list_2[2][0]==com_1 or list_2[2][2]==com_2):
                draw_1 += 1
                point_1 += 1
                draw_2 += 1
                point_2 += 1
        info_1.append(champ_1)
        info_2.append(champ_2)
        info_3.append(champ_3)
        info_1.append(draw_1)
        info_2.append(draw_2)
        info_3.append(draw_3)
        info_1.append(loss_1)
        info_2.append(loss_2)
        info_3.append(loss_3)
        info_1.append(point_1)
        info_2.append(point_2)
        info_3.append(point_3)
    info_all = [info_1,info_2,info_3]
    return info_all

def print_tabl_games(tabl_1):
    print()
    print("Command:         Games:  Vict.:  Draw:   Loss:   Points:")
    elem_1 = '{:<15} {:^7} {:^7} {:^7} {:^7} {:^7} '.format(tabl_1[0][0],tabl_1[0][1],tabl_1[0][2],tabl_1[0][3],tabl_1[0][4],tabl_1[0][4])
    elem_2 = '{:<15} {:^7} {:^7} {:^7} {:^7} {:^7} '.format(tabl_1[1][0],tabl_1[1][1],tabl_1[1][2],tabl_1[1][3],tabl_1[1][4],tabl_1[1][4])
    elem_3 = '{:<15} {:^7} {:^7} {:^7} {:^7} {:^7} '.format(tabl_1[2][0],tabl_1[2][1],tabl_1[2][2],tabl_1[2][3],tabl_1[2][4],tabl_1[2][4])
    print('{}\n{}\n{}\n'.format(elem_1,elem_2,elem_3))      

try:
    list_games = []
    nn = int(input("Enter number games: "))
    list_games = save_games(nn)
    print_games(nn, list_games)
    tabl_games = []
    tabl_games = info_commands(nn, list_games)
    print_tabl_games(tabl_games)
except: print("Input error!")