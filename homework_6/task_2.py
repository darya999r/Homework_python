# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;

# КАЛЬКУЛЯТОР ПРИНИМАЕТ НА ВХОД СТРОКУ ИЗ ТРЕХ ЧИСЕЛ И ДВУХ ЗНАКОВ, ТИПА 23+12*3
# И ВЫДАЕТ РЕЗУЛЬТАТ РАСЧЕТА.

def enter_example():
    example = input("Enter example: ")
    list_ex = list(example)
    # print(list_ex)
    list_temp2 = []
    
    while len(list_ex) > 0:
        list_temp1 = []
        j=0
        number = ''
        k = 0
        for i in range(len(list_ex)):
            if list_ex[i]=='*' or list_ex[i]=='/' or list_ex[i]=='+' or list_ex[i]=='-':
                while j<i: j += 1
                break
            else: list_temp1.append(list_ex[i])
        # print(list_temp1)

        for i in range(len(list_temp1)):
            number += list_temp1[i]
        list_temp2.append(int(number))
        # print(list_temp2)
    
        while k<(len(list_temp1)):
            list_ex.remove(list_ex[0])
            k += 1

        if len(list_ex)>0:
            list_temp2.append(list_ex[0])
            # print(list_temp2)
            list_ex.remove(list_ex[0])
    return list_temp2

def calculation_two_elem(list_1):
    for i in range(len(list_1)):
        if list_1[i] == '*':
            result = list_1[i-1]*list_1[i+1]
        elif list_1[i] == '/':
            result = list_1[i-1]/list_1[i+1]
        elif list_1[i] == '+':
            result = list_1[i-1]+list_1[i+1]
        elif list_1[i] == '-':
            result = list_1[i-1]-list_1[i+1]
    return result

def calculation(list_examp):
    list_1 = []
    for elem in list_examp:
        list_1.append(elem)

    for i in range(len(list_1)):
            if list_1[1]=='*':
                a = 2
            elif list_1[1]=='/':
                a = 2
            elif list_1[3]=='*':
                a = 1
            elif list_1[3]=='/':
                a = 1
            else: a = 2
            
    counter = 0
    while counter<5 and len(list_1)>3:
        for i in range(len(list_1)-a):
            if list_1[i]=='*' and  counter==1:
                temp = list_1[i-1]*list_1[i+1]
                list_1[i-1] = temp
                list_1.remove(list_1[i+1])
                list_1.remove(list_1[i])

            elif list_1[i]=='/' and  counter==2:
                temp = list_1[i-1]/list_1[i+1]
                list_1[i-1] = temp
                list_1.remove(list_1[i+1])
                list_1.remove(list_1[i])

            elif list_1[i]=='+' and  counter==3:
                temp = list_1[i-1]+list_1[i+1]
                list_1[i-1] = temp
                list_1.remove(list_1[i+1])
                list_1.remove(list_1[i])

            elif list_1[i]=='-' and  counter==4:
                temp = list_1[i-1]-list_1[i+1]
                list_1[i-1] = temp
                list_1.remove(list_1[i+1])
                list_1.remove(list_1[i])
        counter += 1
    return list_1



list_task = []
list_task = enter_example()
# print(list_task)
list_1 = calculation(list_task)
# print(list_1)
result = calculation_two_elem(list_1)
print("Result = ", result)




