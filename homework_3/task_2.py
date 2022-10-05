# Задача 2. Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def fillArray (N, array):
    for _ in range(0,N):
        array.append(int(input("Enter number: ")))
    return array

def multiplNumbers (k, arr):
    arr2 = []
    if k%2==0:
        for i in range(len(arr)//2):
            arr2.append(arr[i]*arr[-(i+1)]) 
    if k%2!=0:
        for i in range((len(arr)//2)+1):
            arr2.append(arr[i]*arr[-(i+1)])
    return arr2

try:
    list1 = []
    list2 = []
    n = int(input("Enter the number of numbers: "))
    list1 = fillArray(n,list1)
    print("List of numbers: ", list1)
    list2 = multiplNumbers (n,list1)
    print("Multiplication of elements by pairs: ", list2)
except:
    print("Enter integer numbers!")