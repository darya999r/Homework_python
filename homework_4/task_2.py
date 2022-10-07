# задача 2 . Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

def removeDubleNumbers(array):
    arr = []
    for i in array:
        if i not in arr:
            arr.append(i)
    return arr

list1 = [1, 4, 6, 34, 2, 4, 1, 56, 88, 35, 56, 18]
list2 = []
list2 = removeDubleNumbers(list1)
print(list2)

