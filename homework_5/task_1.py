# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

#  number 1: человек против человека

def draw():
    first_move = int(random.randint(1,3))
    if first_move == 1:
        d = 1
    elif first_move == 2:
        d = 2
    print("firest move: ", d)
    return d

def moves(d,total_score,gamer_1,gamer_2):
    counter_1 = 0
    counter_2 = 0
    while total_score>=0:
        if d==1 and total_score>0:
            if counter_1%2==0 or counter_1==0:
                # moves_1 = int(input("Gamer 1: enter the number of candies: "))
                if total_score>=28:
                    moves_1 = int(random.randint(1,29))
                else:
                    moves_1 = int(random.randint(1,total_score))
                gamer_1 += moves_1
                total_score -= moves_1
                counter_1 += 1
            else:
                # moves_2 = int(input("Gamer 2: enter the number of candies: "))
                if total_score>=28:
                    moves_2 = int(random.randint(1,29))
                else:
                    moves_2 = int(random.randint(1,total_score))
                gamer_2 += moves_2
                total_score -= moves_2
                counter_1 += 1
            print("Total score:",total_score, "Gamer 1:",gamer_1, "Gamer 2:", gamer_2, "Number move:", counter_1)
        elif d==2 and total_score>0:
            if counter_2%2==0 or counter_2==0:
                # moves_2 = int(input("Gamer 2: enter candies at 0 to 28: "))
                if total_score>=28:
                    moves_2 = int(random.randint(1,29))
                else:
                    moves_2 = int(random.randint(1,total_score))
                gamer_2 += moves_2
                total_score -= moves_2
                counter_2 += 1
            else:
                # moves_1 = int(input("Gamer 1: enter candies at 0 to 28: "))
                if total_score>=28:
                    moves_1 = int(random.randint(1,29))
                else:
                    moves_1 = int(random.randint(1,total_score))
                gamer_1 += moves_1
                total_score -= moves_1
                counter_2 += 1
            print("Total score:",total_score, "Gamer 1:",gamer_1, "Gamer 2:", gamer_2, "Number move:", counter_2)
        elif total_score==0:
            if counter_1%2!=0: 
                print("The first gamer won!")
                break
            elif counter_1%2==0: 
                print("The second gamer won!")
                break
            elif counter_2%2!=0: 
                print("The second gamer won!")
                break
            elif counter_2%2==0: 
                print("The first gamer won!")
                break


total_score = 2021
gamer_1 = 0
gamer_2 = 0
d = draw()
# d = 2
moves(d,total_score,gamer_1,gamer_2)


