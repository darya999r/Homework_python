# Задача 1 Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def fillArray (N, array):
    for _ in range(0,N):
        array.append(int(input("Enter number: ")))
    return array

def sumOdd (arr):
    sum = 0
    for i in range(len(arr)):
        if i%2!=0:
            sum += arr[i]
    return sum

try:
    list1 = []
    n = int(input("Enter the number of numbers: "))
    list1 = fillArray(n,list1)
    print("List of numbers: ", list1)
    print("Sum of elements on odd position: ", sumOdd(list1))
except:
    print("Enter integer numbers!")
