# Задача 3. Реализуйте алгоритм перемешивания списка. 
# Список размерностью 10 задается случайными целыми числами, 
# выводится на экран, затем перемешивается, опять выводится на экран. 
# SHUFFLE нельзя юзать!

import random

def fillArr(arr,l):
    arr = []
    for i in range(0, l):
        arr.append(random.randint(0,30))
    return arr

def shufNumbers(array):
    temp = 0
    for i in range(len(array)):
        if i%2==0:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
    return array

list1 = []
length = 10      
list1 = fillArr(list1, length)

print(list1)
print()
print(shufNumbers(list1))


