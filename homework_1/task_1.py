# задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

try:
    number = int(input("Enter number: ")) 
    if 1<=number<=7:
        if number==6 or number==7:
            print("Yes")
        elif 1<=number<=5:
            print("No")
    else:
        print("Enter number between 1 and 7!")
    
except:
    print("Enter an integer!")