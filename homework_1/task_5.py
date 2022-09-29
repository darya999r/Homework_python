# Задача 5 VERY HARD SORT необязательная

# Задайте двумерный массив из целых чисел. 
# Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10


try:
    a = int(input("Enter the numbers of rows: "))
    b = int(input("Enter the number of columns: "))

    import random

    def PrintArray(array):
        for i in range(len(array)):
            for j in range(len(array[i])):
                print(f"{array[i][j]} ", end=' ')
            print()

    arr =[]
    for i in range(a):
        arr.append([])
        for j in range(b):
            arr[i].append(random.randint(1,9))

    PrintArray(arr)
    print()

    arrNew = []
    for k in arr:
        for h in k:
            arrNew.append(h)

    arr = sorted(arrNew)

    for x in range(0,len(arr),b):
        section = arr[x:b+x]
        if len(section)<b:
            section = section + [None for y in range(a-len(section))]
        print(list(section))

except:
    print("Enter integer numbers of rows and columns!")
            