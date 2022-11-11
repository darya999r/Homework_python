# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. 
# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Количество предикатов генерируется случайным образом от 5 до 11, 
# проверяем это утверждение 10 раз, с помощью модуля time выводим на экран, 
# сколько времени отработала программа.

from random import *
import time
ar = [True,False]    
start = time.time()

def CheckPredicates():
    num=randint(5,11)
    array = [choice(ar) for _ in range(num) ]
    print(array)
    res1=array[0]     # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
    res2= not array[0]
    for i in range(1,len(array) - 1):
        res1=res1 or array[i]
        res2=res2 and not array[i] 
    if not res1 == res2: return True
    else: return False
    

for _ in range(10):
    rez=CheckPredicates()
    if rez: print("Утверждение верно")
    else: print("не получилось")
fin = time.time()
print("заняло времени", fin - start)
