# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. 
# Напишите программу, которая принимает на вход N, 
# и координаты двух точек и находит 
# расстояние между ними в N-мерном пространстве.

def enterX(n):
    listX = []
    for i in range(1, n+1):
        listX.append(float(input("Enter the coordinates of the first point: ")))
    return listX

def enterY(n):
    listY = []
    for i in range(1, n+1):
        listY.append(float(input("Enter the coordinates of the second point: ")))
    return listY

def distansEuclid(n, arr1, arr2):
    res = 0
    sum = 0
    counter = 0
    while counter<=(n-1):
        res = (arr2[counter]-arr1[counter])**2
        sum += res
        counter += 1
    res1 = sum**0.5
    return res1

try:
    N = int(input("Enter number N: "))

    list1 = enterX(N)
    list2 = enterY(N)
    print("Coordinates of the first point: ", list1)
    print("Coordinates of the second point: ", list2)

    result = distansEuclid(N,list1,list2)
    print("Distance between two points: ", round(result,3))
except:
    print("For N: enter integer number!"
    +"\nFor coordinates: enter integer or float numbers!")
