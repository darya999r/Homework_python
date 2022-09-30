# Задача 2. Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def fillArr(num, arr):
    arr = []
    for i in range(1,num+1):
        arr.append(i)
    return arr

def prodNum(arr1):
    for i in range(len(arr1)):
        if i==0:
            arr1[i] = 1
        else:
            arr1[i] = arr1[i-1] * (i+1)
    return arr1

try:
    number = int(input("Enter number N: "))
    array = []
    array = fillArr(number, array)
    print("Product of numbers from 1 to N: ", prodNum(array))
except:
    print("Enter integer number!")