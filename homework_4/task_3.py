# задача 3. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def randomCoeffitients(N):
    array = []
    for _ in range(N+1):
        array.append(random.randint(0,100))
    return array

def polynom(arr, n):
    poly3 = []
    if n>0:
        while n!=1:
            if arr[0]==0:
                poly1 = [arr[1],'*','x']
                poly2 = [arr[n], '*', 'x', '^', n, '+']
                poly3 = poly3 + poly2
            elif arr[1]==0:
                poly1 = ['+',arr[0]]
                poly2 = [arr[n], '*', 'x', '^', n, '+']
                poly3 = poly3 + poly2
            elif arr[n]==0:
                poly1 = [arr[1],'*','x','+',arr[0]]
                poly2 = []
                poly3 = poly3 + poly2
            elif arr[n]!=0:
                poly1 = [arr[1],'*','x','+',arr[0]]
                poly2 = [arr[n], '*', 'x', '^', n, '+']
                poly3 = poly3 + poly2
            n-=1
        poly3 = poly3 + poly1
    elif n==0:
        print("The polynomial has no solutions!")
    else: print("Input error!")
    return poly3

def writingToFile (list1):
    data = open('file_for_task3.txt', 'w')
    data.write(list1)
    data.close()
    return print("The polynomial is written to a file!")


try:
    k = int(input("Enter number k: "))
    coef = randomCoeffitients(k)
    
    if k!=1 and k>0: 
        print("Coeffitients of polynomial: ", coef)
        polyResult = polynom(coef, k)
        polyResult.append('= 0')
        print(polyResult)
        result = " ".join(map(str, polyResult))
        writingToFile(result)   
    elif k==1: print("The polynomial has no solutions!")
    elif k<0: print("Input error!")

except: print("Input error!")




