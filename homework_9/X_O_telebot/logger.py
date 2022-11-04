from datetime import datetime as dt
import telebot

def datetime (name:str, winner:str):
    time = dt.now().strftime('%d/%m/%Y %H:%M')
    with open ('xo_telebot\log.csv', 'a', encoding="utf-8") as file:
        file.write(f'ДатаВремя:{time}, ИмяИгрока:{name}, Результат:{winner}\n')

def view_log():
    with open('xo_telebot\log.csv', 'r', encoding="utf-8") as data:
        list_1 = []
        list_2 = []
        for line in data:
            list_1.append(line)
        list_2.append(list_1[-6:-1])
        data_str = "\n".join(map(str,list_2))
        return data_str
            
def clear_log():
    data = open ('xo_telebot\log.csv', 'w', encoding="utf-8")
    data.close()

