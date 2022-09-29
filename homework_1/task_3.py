# задача 3. Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))

    if x!=0 and y!=0:
        if x>0 and y>0:
            print("1 quarter")
        elif x<0 and y>0:
            print("2 quarter")
        elif x<0 and y<0:
            print("3 quarter")
        elif x>0 and y<0:
            print("4 quarter")
    elif x==0 and y!=0:
        print("The point is on the y-axis!")
    elif x!=0 and y==0:
        print("The point is on the x-axis!")

except:
    print("Enter the numeric values of x and y!")