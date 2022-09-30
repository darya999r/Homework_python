# Задача 1. Напишите программу, которая принимает на вход 
# вещественное или целое число и показывает сумму его цифр. 
# Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11


def getArray(num, arr):   #заполняем массив цифрами из числа
    while num>0:
        arr.append(num%10)
        num //= 10
    arr.reverse()
    return arr

def sumNumbers(array):   #сумма чисел массива(заданного числа)
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum


try:
    number = input("Enter number: ")
    tempNum = float(number.replace('.', ''))   #убираем запятую в десятичной дроби
    number = int(tempNum)

    array = []
    getArray(number, array)

    print("Sum of numbers: ", sumNumbers(array))

except:
     print("Enter the integer or float number!!!"
     +"\nfor example: 245 or 5.45")


