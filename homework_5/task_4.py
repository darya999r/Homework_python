# задача 4 необязательная 
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def read_file (file_name):
    with open (file_name, 'r', encoding="utf-8") as file:
        for data in file:
            print(data, end="\n")
    file.close()
    return data

def write_file (file_name, list_1):
    data = open(file_name, 'w', encoding="utf-8")
    data.write(list_1)
    data.close()
    return print("The sum of polynomiales is written to a file!")

f_name_1 = 'file_1_task4.txt'
f_name_2 = 'file_2_task4.txt'

print("First polynomial:")
str_1 = read_file(f_name_1)

print("Second polynomial:")
str_2 = read_file(f_name_2)

list_1 = list(str_1.split(' '))
list_2 = list(str_2.split(' '))

# print(list_1)
# print(list_2)

list_coef = []

for i in range(len(list_1)):
    if list_1[i]=='*' or list_1[i]=='=':
        sum_coef = int(list_1[i-1]) + int(list_2[i-1])
        list_coef.append(sum_coef)
list_coef.reverse()


# print(list_coef)


n = 3
poly_n = []
if n>0:
    while n!=1:
        poly_1 = [list_coef[1],'*','x','+',list_coef[0],'=','0']
        poly_2 = [list_coef[n], '*', 'x', '^', n, '+']
        poly_n = poly_n + poly_2
        n -= 1
    poly_n = poly_n + poly_1
else: print("Error!")

# print(poly_n)

list_sum = " ".join(map(str,poly_n))
print("Sum of polinomiales:")
print(list_sum)
f_name_3 = 'file_3_task4.txt'
write_file (f_name_3, list_sum)
    


