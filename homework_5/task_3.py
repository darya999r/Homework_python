# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

list_1 = 'Читабвйте самые интересные и обсуждабвемые посты по теме Текст. Личный опыт, познавабвтельные статьи, забвавные фото и видео. Или поделитесь своей историей.'
print("Specified text:\n", list_1)
list_2 = list(list_1.split(' '))
searching = 'абв'
for elem in list_2:
    if searching in elem:
        list_2.remove(elem)

print("Corrected text:")
print(" ".join(map(str,list_2)))