# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n 
# (размерность вводим с клавиатуры) , причем чтоб количество 
# элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, 
# причем чтобы каждый гарантированно переместился на другое место 
# и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, 
# то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.

import random

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))


def getArray (N, M):   #создаём пустой массив заданного размера
    arr = []
    for _ in range(N):
        arr.append([0]*M)
    return arr

def fillArray (arr):    #заполняем массив случайными числами
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = random.randint(0,30)
    return arr

def printArray (array):     #выводим массив в терминал
    for row in array:
        for elem in row:
            print(elem, end='\t')
        print()

def moveElements (matr):    #перемешиваем элементы случайным образом за n*m/2 итераций
    k = 1                       
    while k<((n*m//2)):
        r1 = random.randint(0,n-1)
        r2 = random.randint(0,n-1)
        c1 = random.randint(0,m-1)
        c2 = random.randint(0,m-1)

        temp = matr[r1][c1]
        matr[r1][c1] = matr[r2][c2]
        matr[r2][c2] = temp
        k+=1
    print(k)
    return matr

try:
    if (n*m)%2==0:
        matrix1 = fillArray(getArray(n, m))
        print("First array:")
        printArray(matrix1)
        print()
        matrix2 = moveElements(matrix1)
        print("Second array:")
        printArray(matrix2)
    else: print("The numbers of elements n*m should be even!")
except:
    print("Input error!")