# задача 4 необязательная 
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# вариант решения только с положительными коэффициентами:

def read_file (file_name):   #чтение файла
    with open (file_name, 'r', encoding="utf-8") as file:
        for data in file:
            print(data, end="\n")
    file.close()
    return data

def write_file (file_name, list_1):   #запись файла
    data = open(file_name, 'w', encoding="utf-8")
    data.write(list_1)
    data.close()
    return print("The sum of polynomiales is written to a file!")

def list_coef_sum (list1, list2):   #список суммы коэффициентов многочленов
    for i in range(len(list1)):
        if list1[i]=='*' or list1[i]=='=':
            sum_coef = int(list1[i-1]) + int(list2[i-1])
            list_coef.append(sum_coef)
    list_coef.reverse()
    return list_coef

def max_degree_poly (list1, list2):   #максимальная степень х
    for _ in list1:
        if int(list1[4]) > int(list2[4]):
            n = int(list1[4])
        else:
            n = int(list2[4])
    return n

def maximizing_poly (list1, n):    #увеличиваем многочлен до максимальной степени(добавляем нули вместо коэффициентов)
    a1 = int(list1[4])
    counter1 = 1
    list_dif_1 = []
    while n >= (a1+counter1):
        list_dif_1 = ['0','*','x','^',str(a1+counter1),'+'] + list_dif_1
        counter1 += 1
    list1 = list_dif_1 + list1
    return list1
        

def fill_poly (list_coef, n):   #заполняем список с суммой многочленов
    poly_3 = []
    if n>0:
        while n!=1:
            poly_1 = [list_coef[1],'*','x','+',list_coef[0],'=','0']
            poly_2 = [list_coef[n], '*', 'x', '^', n, '+']
            poly_3 = poly_3 + poly_2
            n -= 1
        poly_3 = poly_3 + poly_1
    else: print("Error!")
    return poly_3

try:
    f_name_1 = 'file_1_task4.txt'
    f_name_2 = 'file_2_task4.txt'
    f_name_3 = 'file_3_task4.txt'

    print("First polynomial:")
    str_1 = read_file(f_name_1)

    print("Second polynomial:")
    str_2 = read_file(f_name_2)

    list_1 = list(str_1.split(' '))
    list_2 = list(str_2.split(' '))

    # print(list_1)
    # print(list_2)

    n = max_degree_poly(list_1, list_2)
    # print(n)

    if int(list_1[4])>int(list_2[4]): list_2 = maximizing_poly (list_2, n)
    else: list_1 = maximizing_poly (list_1, n)
    # print(list_1)
    # print(list_2)

    list_coef = []
    list_coef = list_coef_sum (list_1, list_2)
    # print(list_coef)
    
    poly_n = []
    poly_n = fill_poly (list_coef, n)
    # print(poly_n)

    list_sum = " ".join(map(str,poly_n))
    print("Sum of polinomiales:")
    print(list_sum)

    write_file (f_name_3, list_sum)

except: print("Files are empty or written incorrectly!\nAll characters must be written with a space!")
    


