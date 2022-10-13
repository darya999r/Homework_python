# задача 5 необязательная 
# Дан список чисел. Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. 
# Порядок элементов менять нельзя.

# *Пример:* 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 
# [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]

def list_sequence_num (list_1, temp):
    new_list = []
    counter = 0
    while counter < len(list_1):
        for i in range(len(list_1)):
            if (list_1[i]-temp) == 1:
                new_list.append(list_1[i])
                temp = list_1[i]
        counter += 1
    return new_list

try:
    list_num = [1, 5, 2, 3, 4, 1, 7, 8, 15, 1]
    # list_num = [1, 5, 2, 3, 4, 1, 7, 8, 15, 1, 9, 10, 11]
    # list_num = [1, 3, 5, 7, 3, 9, 15]
    sequence_num = []
    sequence_num_next = []
    list_res = []

    t = 0
    sequence_num = list_sequence_num(list_num, t)
    if len(sequence_num)<2:
        sequence_num = []
    else:
        print("First sequence: ", sequence_num)

    t = (sequence_num[-1]+1)
    sequence_num_next = list_sequence_num(list_num, t)
    if len(sequence_num_next)<2:
        sequence_num_next = []
    else:
        print("Second sequence: ", sequence_num_next)

    if len(sequence_num)>len(sequence_num_next):
        list_res.append(sequence_num[0])
        list_res.append(sequence_num[-1])
    elif len(sequence_num)<len(sequence_num_next):
        list_res.append(sequence_num_next[0])
        list_res.append(sequence_num_next[-1])
    else:
        print("There are two solutions: ")
        list_1 = []
        list_2 = []
        list_1.append(sequence_num[0])
        list_1.append(sequence_num[-1])
        list_2.append(sequence_num_next[0])
        list_2.append(sequence_num_next[-1])
        list_res = [list_1, list_2]
    print("Solution: ", list_res)
except: print("The list has no sequences!")




