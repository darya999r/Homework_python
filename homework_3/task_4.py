# Задача 4. Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convertNumber(N):
    arr = []
    while N>0:
        res = N%2
        arr.append(res)
        N = N//2
    arr.reverse()
    return arr

try:
    n = int(input("Enter number: "))
    list1 = convertNumber(n)
    print("".join(map(str, list1)))
except:
    print("Enter an integer!")