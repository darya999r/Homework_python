# Задача 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fillArray (N, array):
    for _ in range(0,N):
        array.append(float(input("Enter number: ")))
    return array

def fractionalPartNumbers (arr):
    arr2 = []
    for i in range(len(arr)):
        temp1 = arr[i]
        temp2 = int(arr[i])
        res = temp1 - temp2
        res = round(res, 2)
        arr2.append(res)
    return arr2

def maxPartNumbers (array1):
    maxNum = array1[0]
    for i in range(len(array1)):
        if maxNum<array1[i]:
            maxNum = array1[i]
    return maxNum

def minPartNumbers (array2):
    minNum = array2[0]
    for i in range(len(array2)):
        if minNum>array2[i]:
            minNum = array2[i]
    return minNum

try:
    n = int(input("Enter the number of numbers: "))

    list1 = []
    list1 = fillArray(n,list1)
    print("List of numbers: ", list1)
    
    list2 = []
    list2 = fractionalPartNumbers(list1)
    print("Fractional part of numbers: ", list2)

    diffPartNumbers = maxPartNumbers(list2) - minPartNumbers(list2)
    print("Difference between the value of parts: ", round(diffPartNumbers, 2))
except:
    print("Input error!")