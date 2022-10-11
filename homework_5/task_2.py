# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def read_file (file_name):
    print("Read data:")
    with open (file_name, 'r', encoding="utf-8") as file:
        for data in file:
            print(data, end="")
    file.close()
    return data

def write_file (file_name, data):
    with open (file_name, 'w', encoding="utf-8") as file:
        file.write(data)
    file.close()
    return print("File overwritten!")

def compression_data (data):
    data_result = ''
    single_element = ''
    counter = 1
    for elem in data:
        if elem != single_element:
            if counter == 1 and single_element=='':
                single_element = elem
            else:
                data_result += str(counter) + single_element
                counter = 1
                single_element = elem
        else:
            counter += 1
    else:
        data_result += str(counter) + single_element
        return data_result
    


try:
    f_name_1 = 'file_1_task2.txt'
    data_1 = read_file(f_name_1)
    print()
    data_2 = compression_data(data_1)
    print("RLE compression data: ")
    print(data_2)
    f_name_2 = 'file_2_task2.txt'
    write_file (f_name_2, data_2)
except: print("The file is empty!")


