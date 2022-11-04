import telebot
from telebot import types
import json
import requests

API_TOKEN='tokentoken'
bot = telebot.TeleBot(API_TOKEN)

print('bot is start')

def view_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as fl:
        file_1 = json.load(fl)
    return file_1

def get_img_1(img_url):
    image = requests.get(img_url)
    with open('new_image_1.jpg', 'wb') as f:
        f.write(image.content)
    file = 'new_image_1.jpg'
    return file

def get_img_2(img_url):
    image = requests.get(img_url)
    with open('new_image_2.jpg', 'wb') as f:
        f.write(image.content)
    file = 'new_image_2.jpg'
    return file

@bot.message_handler(commands=['start'])
def startMessage(message):
    key = {}
    keyboard_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    key[0] = types.KeyboardButton("О кето диете")
    key[1] = types.KeyboardButton("Противопоказания кето диеты!!!")
    key[2] = types.KeyboardButton("Какие продукты можно")
    key[3] = types.KeyboardButton("Каких продуктов стоит избегать")
    key[4] = types.KeyboardButton("Кето-меню на каждый день")
    keyboard_1.row(key[0], key[1])
    keyboard_1.row(key[2], key[3])
    keyboard_1.row(key[4])

    name = message.from_user.first_name
    bot.send_message(message.chat.id,f"Привет, {name}! Я Шеф_кето_бот!\nГотов помочь тебе с кето-диетой.", parse_mode='html', reply_markup=keyboard_1)

@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.chat.type == 'private':
        if message.text == "О кето диете":
            markup_1 = types.InlineKeyboardMarkup(row_width=1)
            but1 = types.InlineKeyboardButton("Кетогенная диета", callback_data='text1')
            but2 = types.InlineKeyboardButton("Что такое кетоз", callback_data='text2')
            but3 = types.InlineKeyboardButton("Как быстро войти в кетоз", callback_data='text3')
            but4 = types.InlineKeyboardButton("Как понять, что я в кетозе", callback_data='text4')
            but5 = types.InlineKeyboardButton("Возможные побочные эффекты", callback_data='text5')
            markup_1.add(but1,but2,but3,but4,but5)
            bot.send_message(chat_id=message.chat.id, text="Что тебе рассказать?", reply_markup=markup_1)
        elif message.text == "Противопоказания кето диеты!!!":
            file_name = 'about_diet.json'
            about_keto = view_text(file_name)
            bot.send_message(chat_id=message.chat.id, text=about_keto[10])
        elif message.text == "Какие продукты можно":
            bot.send_message(message.chat.id, 'Цифры означают — количество углеводов/100 грамм. Полностью допустимы продукты с зелеными надписями, оранжевые - с ограничением, красные - необходимо избегать!')

            photo1 = open('img\keto-diet-guide.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo1)
            
            photo2 = open('img\Vegetable-sticks2-ру-1-1300x642.png', 'rb')
            bot.send_photo(message.chat.id, photo=photo2)
            
            photo3 = open('img\Keto-vegetables-AG-ру-1300x586.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo3)
            
            photo4 = open('img\keto_3.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo4)
            
            photo5 = open('img\LC-Fats-Sauces-2_170506_2.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo5)
            
            photo6 = open('img\keto_1.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo6)
            
            photo7 = open('img\Keto-drinks1.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo7)
            
            photo8 = open('img\imgonline-com-ua-dexifdZt18EuN4iBj.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo8)
        
        elif message.text == "Каких продуктов стоит избегать":
            bot.send_message(message.chat.id, 'Цифры означают — количество углеводов/100 грамм. Продуктов с красными надписями нужно избегать!')

            photo9 = open('img\Grains-sugar-1-ру-1-1300x427.png', 'rb')
            bot.send_photo(message.chat.id, photo=photo9)
            
            photo10 = open('img\Keto-vegetables-BG-3-ру-1-1300x419.png', 'rb')
            bot.send_photo(message.chat.id, photo=photo10)
            
            photo11 = open('img\keto_2.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo11)
            
            photo12 = open('img\Peas-beans-lentils-quinoa-corn-ру-1-1300x476.png', 'rb')
            bot.send_photo(message.chat.id, photo=photo12)
            
            photo13 = open('img\Keto-Chocolate-Snacks-1.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo13)
            
            photo14 = open('img\LC-Drinks_edited2_2400-ру-1-889x1024.png', 'rb')
            bot.send_photo(message.chat.id, photo=photo14)

        elif message.text == "Кето-меню на каждый день":
            markup_menu = types.InlineKeyboardMarkup(row_width=3)
            but1 = types.InlineKeyboardButton("Понедельник", callback_data='menu1')
            but2 = types.InlineKeyboardButton("Вторник", callback_data='menu2')
            but3 = types.InlineKeyboardButton("Среда", callback_data='menu3')
            but4 = types.InlineKeyboardButton("Четверг", callback_data='menu4')
            but5 = types.InlineKeyboardButton("Пятница", callback_data='menu5')
            but6 = types.InlineKeyboardButton("Суббота", callback_data='menu6')
            but7 = types.InlineKeyboardButton("Воскресенье", callback_data='menu7')
            markup_menu.add(but1,but2,but3,but4,but5,but6,but7)
            bot.send_message(chat_id=message.chat.id, text="Меню рассчитано на два приёма пищи. Выбери день недели", reply_markup=markup_menu)
        else:
            bot.send_message(message.chat.id, "Я не знаю таких слов :(")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

        if call.message:
            file_name = 'about_diet.json'
            about_keto = view_text(file_name)
            if call.data == 'text1':
                bot.send_message(call.message.chat.id, about_keto[0])
            elif call.data == 'text2':
                bot.send_message(call.message.chat.id, about_keto[1])
            elif call.data == 'text3':
                bot.send_message(call.message.chat.id, about_keto[2])
                markup_2 = types.InlineKeyboardMarkup(row_width=2)
                b1 = types.InlineKeyboardButton("1.Ограничьте потребление углеводов", callback_data='num1')
                b2 = types.InlineKeyboardButton("2.Ограничьте белок до умеренного количества", callback_data='num2')
                b3 = types.InlineKeyboardButton("3.Потребляйте достаточно жиров", callback_data='num3')
                b4 = types.InlineKeyboardButton("4.Избегайте перекусов", callback_data='num4')
                b5 = types.InlineKeyboardButton("5.Можно добавить интервальное голодание", callback_data='num5')
                b6 = types.InlineKeyboardButton("6.Добавьте физическую нагрузку", callback_data='num6')
                b7 = types.InlineKeyboardButton("7.Спите достаточно", callback_data='num7')
                markup_2.add(b1,b2,b3,b4,b5,b6,b7)
                bot.send_message(chat_id=call.message.chat.id, text="Вот семь самых важных вещей для входа в состояние кетоза, ранжированные от самых важных до менее важных:", reply_markup=markup_2)
            elif call.data =='num1':
                bot.send_message(call.message.chat.id, about_keto[11])
            elif call.data =='num2':
                bot.send_message(call.message.chat.id, about_keto[12])
            elif call.data =='num3':
                bot.send_message(call.message.chat.id, about_keto[13])
            elif call.data =='num4':
                bot.send_message(call.message.chat.id, about_keto[14])
            elif call.data =='num5':
                bot.send_message(call.message.chat.id, about_keto[15])
            elif call.data =='num6':
                bot.send_message(call.message.chat.id, about_keto[16])
            elif call.data =='num7':
                bot.send_message(call.message.chat.id, about_keto[17])
            elif call.data == 'text4':
                bot.send_message(call.message.chat.id, about_keto[3])
                markup_3 = types.InlineKeyboardMarkup(row_width=3)
                b1 = types.InlineKeyboardButton("Сухость во рту и постоянная жажда", callback_data='t1')
                b2 = types.InlineKeyboardButton("Частое мочеиспускание", callback_data='t2')
                b3 = types.InlineKeyboardButton("Кето-дыхание", callback_data='t3')
                b4 = types.InlineKeyboardButton("Снижение аппетита", callback_data='t4')
                b5 = types.InlineKeyboardButton("Повышение уровня энергии", callback_data='t5')
                markup_3.row(b1)
                markup_3.row(b2,b3)
                markup_3.row(b4,b5)
                bot.send_message(chat_id=call.message.chat.id, text="Eсть также явные симптомы нахождения в кетозе:", reply_markup=markup_3)
            elif call.data == 't1':
                bot.send_message(call.message.chat.id, about_keto[5])
            elif call.data == 't2':
                bot.send_message(call.message.chat.id, about_keto[6])
            elif call.data == 't3':
                bot.send_message(call.message.chat.id, about_keto[7])
            elif call.data == 't4':
                bot.send_message(call.message.chat.id, about_keto[8])
            elif call.data == 't5':
                bot.send_message(call.message.chat.id, about_keto[9])
            elif call.data == 'text5':
                bot.send_message(call.message.chat.id, about_keto[4])
            elif call.data == 'menu1':
                bot.send_message(call.message.chat.id, 'Завтрак: Сырно-яичные кето-вафли')
                get_img_1(img_url='https://ketoblog.ru/wp-content/uploads/2021/08/%D0%A1%D1%8B%D1%80%D0%BD%D0%BE-%D1%8F%D0%B8%D1%87%D0%BD%D1%8B%D0%B5-%D0%BA%D0%B5%D1%82%D0%BE-%D0%B2%D0%B0%D1%84%D0%BB%D0%B8-%D0%BD%D0%B0-%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0%D0%BA-1300x867.jpg')
                photo_1 = open('new_image_1.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_1)
                response_1 = requests.get('https://ketoblog.ru/recipe/syrno-jaichnye-keto-vafli-na-zavtrak/')
                recipe1_url = response_1.url
                bot.send_message(call.message.chat.id, recipe1_url)
                
                bot.send_message(call.message.chat.id, 'Обед/Ужин: Итальянские куриные фрикадельки со сливочным соусом и брокколи')
                get_img_2(img_url='https://ketoblog.ru/wp-content/uploads/2021/08/%D0%98%D1%82%D0%B0%D0%BB%D1%8C%D1%8F%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%BA%D1%83%D1%80%D0%B8%D0%BD%D1%8B%D0%B5-%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%B4%D0%B5%D0%BB%D1%8C%D0%BA%D0%B8-%D1%81%D0%BE-%D1%81%D0%BB%D0%B8%D0%B2%D0%BE%D1%87%D0%BD%D1%8B%D0%BC-%D1%81%D0%BE%D1%83%D1%81%D0%BE%D0%BC-%D0%B8-%D0%B1%D1%80%D0%BE%D0%BA%D0%BA%D0%BE%D0%BB%D0%B8-1300x867.jpg')
                photo_2 = open('new_image_2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_2)
                response_2 = requests.get('https://ketoblog.ru/recipe/italjanskie-kurinye-frikadelki-so-slivochnym-sousom-i-brokkoli/')
                recipe2_url = response_2.url
                bot.send_message(call.message.chat.id, recipe2_url)

            elif call.data == 'menu2':
                bot.send_message(call.message.chat.id, 'Завтрак: Кето-фриттата с грибами и сыром')
                get_img_1(img_url='https://ketoblog.ru/wp-content/uploads/2021/08/%D0%9A%D0%B5%D1%82%D0%BE-%D1%84%D1%80%D0%B8%D1%82%D1%82%D0%B0%D1%82%D0%B0-%D1%81-%D0%B3%D1%80%D0%B8%D0%B1%D0%B0%D0%BC%D0%B8-%D0%B8-%D1%81%D1%8B%D1%80%D0%BE%D0%BC-1-1300x867.jpg')
                photo_1 = open('new_image_1.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_1)
                response_1 = requests.get('https://ketoblog.ru/recipe/keto-frittata-s-gribami-i-syrom/')
                recipe1_url = response_1.url
                bot.send_message(call.message.chat.id, recipe1_url)
                
                bot.send_message(call.message.chat.id, 'Обед/Ужин: Пряная тушеная кето-говядина с жареным рисом из цветной капусты')
                get_img_2(img_url='https://ketoblog.ru/wp-content/uploads/2021/08/%D0%9F%D1%80%D1%8F%D0%BD%D0%B0%D1%8F-%D1%82%D1%83%D1%88%D0%B5%D0%BD%D0%B0%D1%8F-%D0%BA%D0%B5%D1%82%D0%BE-%D0%B3%D0%BE%D0%B2%D1%8F%D0%B4%D0%B8%D0%BD%D0%B0-%D1%81-%D0%B6%D0%B0%D1%80%D0%B5%D0%BD%D1%8B%D0%BC-%D1%80%D0%B8%D1%81%D0%BE%D0%BC-%D0%B8%D0%B7-%D1%86%D0%B2%D0%B5%D1%82%D0%BD%D0%BE%D0%B9-%D0%BA%D0%B0%D0%BF%D1%83%D1%81%D1%82%D1%8B-1300x867.jpg')
                photo_2 = open('new_image_2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_2)
                response_2 = requests.get('https://ketoblog.ru/recipe/prjanaja-tushenaja-keto-govjadina-s-zharenym-risom-iz-cvetnoj-kapusty/')
                recipe2_url = response_2.url
                bot.send_message(call.message.chat.id, recipe2_url)    
            
            elif call.data == 'menu3':
                bot.send_message(call.message.chat.id, 'Завтрак: Кето-пицца на тортилье')
                get_img_1(img_url='https://ketoblog.ru/wp-content/uploads/2021/08/%D0%9A%D0%B5%D1%82%D0%BE-%D0%BF%D0%B8%D1%86%D1%86%D0%B0-%D0%BD%D0%B0-%D1%82%D0%BE%D1%80%D1%82%D0%B8%D0%BB%D1%8C%D0%B5-1300x867.jpg')
                photo_1 = open('new_image_1.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_1)
                response_1 = requests.get('https://ketoblog.ru/recipe/keto-picca-na-tortile/')
                recipe1_url = response_1.url
                bot.send_message(call.message.chat.id, recipe1_url)
                
                bot.send_message(call.message.chat.id, 'Обед/Ужин: Мясной кето-рулет с сыром и барбекю-майонезом')
                get_img_2(img_url='https://ketoblog.ru/wp-content/uploads/2021/08/%D0%9C%D1%8F%D1%81%D0%BD%D0%BE%D0%B9-%D0%BA%D0%B5%D1%82%D0%BE-%D1%80%D1%83%D0%BB%D0%B5%D1%82-%D1%81-%D1%81%D1%8B%D1%80%D0%BE%D0%BC-%D0%B8-%D0%B1%D0%B0%D1%80%D0%B1%D0%B5%D0%BA%D1%8E-%D0%BC%D0%B0%D0%B9%D0%BE%D0%BD%D0%B5%D0%B7%D0%BE%D0%BC-1300x867.jpg')
                photo_2 = open('new_image_2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_2)
                response_2 = requests.get('https://ketoblog.ru/recipe/mjasnoj-keto-rulet-s-syrom-i-barbekju-majonezom/')
                recipe2_url = response_2.url
                bot.send_message(call.message.chat.id, recipe2_url)

            elif call.data == 'menu4':
                bot.send_message(call.message.chat.id, 'Завтрак: Кето-закуска из индейки')
                get_img_1(img_url='https://ketoblog.ru/wp-content/uploads/2019/08/DD-481-ketoturkey-2-1300x867.jpg')
                photo_1 = open('new_image_1.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_1)
                response_1 = requests.get('https://ketoblog.ru/recipe/keto-zakuska-iz-indejki/')
                recipe1_url = response_1.url
                bot.send_message(call.message.chat.id, recipe1_url)
                
                bot.send_message(call.message.chat.id, 'Обед/Ужин: Белая рыба на гриле с кабачком и песто из кейла')
                get_img_2(img_url='https://ketoblog.ru/wp-content/uploads/2021/08/%D0%91%D0%B5%D0%BB%D0%B0%D1%8F-%D1%80%D1%8B%D0%B1%D0%B0-%D0%BD%D0%B0-%D0%B3%D1%80%D0%B8%D0%BB%D0%B5-%D1%81-%D0%BA%D0%B0%D0%B1%D0%B0%D1%87%D0%BA%D0%BE%D0%BC-%D0%B8-%D0%BF%D0%B5%D1%81%D1%82%D0%BE-%D0%B8%D0%B7-%D0%BA%D0%B5%D0%B9%D0%BB%D0%B0-1300x867.jpg')
                photo_2 = open('new_image_2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_2)
                response_2 = requests.get('https://ketoblog.ru/recipe/belaja-ryba-na-grile-s-kabachkom-i-pesto-iz-kejla/')
                recipe2_url = response_2.url
                bot.send_message(call.message.chat.id, recipe2_url)

            elif call.data == 'menu5':
                bot.send_message(call.message.chat.id, 'Завтрак: Французские кето-блины')
                get_img_1(img_url='https://ketoblog.ru/wp-content/uploads/2020/06/%D0%A4%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D1%81%D0%BA%D0%B8%D0%B5-%D0%BA%D0%B5%D1%82%D0%BE-%D0%B1%D0%BB%D0%B8%D0%BD%D1%8B-1300x867.jpg')
                photo_1 = open('new_image_1.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_1)
                response_1 = requests.get('https://ketoblog.ru/recipe/francuzskie-keto-bliny/')
                recipe1_url = response_1.url
                bot.send_message(call.message.chat.id, recipe1_url)
                
                bot.send_message(call.message.chat.id, 'Обед/Ужин: Кето-курица с запеченными овощами трех цветов')
                get_img_2(img_url='https://ketoblog.ru/wp-content/uploads/2021/08/%D0%9A%D0%B5%D1%82%D0%BE-%D0%BA%D1%83%D1%80%D0%B8%D1%86%D0%B0-%D1%81-%D0%B7%D0%B0%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8-%D0%BE%D0%B2%D0%BE%D1%89%D0%B0%D0%BC%D0%B8-%D1%82%D1%80%D0%B5%D1%85-%D1%86%D0%B2%D0%B5%D1%82%D0%BE%D0%B2-1300x867.jpg')
                photo_2 = open('new_image_2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_2)
                response_2 = requests.get('https://ketoblog.ru/recipe/keto-kurica-s-zapechennymi-ovoshhami-treh-cvetov/')
                recipe2_url = response_2.url
                bot.send_message(call.message.chat.id, recipe2_url)
                
            elif call.data == 'menu6':
                bot.send_message(call.message.chat.id, 'Завтрак: Кокосовая каша')
                get_img_1(img_url='https://ketoblog.ru/wp-content/uploads/2019/08/Keto-coconut-porridge8-h-1300x867.webp')
                photo_1 = open('new_image_1.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_1)
                response_1 = requests.get('https://ketoblog.ru/recipe/kokosovaja-kasha/')
                recipe1_url = response_1.url
                bot.send_message(call.message.chat.id, recipe1_url)
                
                bot.send_message(call.message.chat.id, 'Обед/Ужин: Рыбная кето-запеканка с грибами и дижонской горчицей')
                get_img_2(img_url='https://ketoblog.ru/wp-content/uploads/2021/08/%D0%A0%D1%8B%D0%B1%D0%BD%D0%B0%D1%8F-%D0%BA%D0%B5%D1%82%D0%BE-%D0%B7%D0%B0%D0%BF%D0%B5%D0%BA%D0%B0%D0%BD%D0%BA%D0%B0-%D1%81-%D0%B3%D1%80%D0%B8%D0%B1%D0%B0%D0%BC%D0%B8-%D0%B8-%D0%B4%D0%B8%D0%B6%D0%BE%D0%BD%D1%81%D0%BA%D0%BE%D0%B9-%D0%B3%D0%BE%D1%80%D1%87%D0%B8%D1%86%D0%B5%D0%B9-1300x866.jpg')
                photo_2 = open('new_image_2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_2)
                response_2 = requests.get('https://ketoblog.ru/recipe/rybnaja-keto-zapekanka-s-gribami-i-dizhonskoj-gorchicej/')
                recipe2_url = response_2.url
                bot.send_message(call.message.chat.id, recipe2_url)

            elif call.data == 'menu7':
                bot.send_message(call.message.chat.id, 'Завтрак: Сырные кето-рулетики')
                get_img_1(img_url='https://ketoblog.ru/wp-content/uploads/2019/07/1task.-%D0%9A%D0%B5%D1%82%D0%BE-%D1%80%D1%83%D0%BB%D0%B5%D1%82%D0%B8%D0%BA%D0%B8-1300x867.jpg')
                photo_1 = open('new_image_1.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_1)
                response_1 = requests.get('https://ketoblog.ru/recipe/syrnye-keto-ruletiki/')
                recipe1_url = response_1.url
                bot.send_message(call.message.chat.id, recipe1_url)
                
                bot.send_message(call.message.chat.id, 'Обед/Ужин: Крабовые кето-котлетки с огуречным салатом')
                get_img_2(img_url='https://ketoblog.ru/wp-content/uploads/2020/06/Keto-crab-cakes-with-cucumber-salad-min-1300x866.jpg')
                photo_2 = open('new_image_2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_2)
                response_2 = requests.get('https://ketoblog.ru/recipe/krabovye-keto-kotletki-s-ogurechnym-salatom/')
                recipe2_url = response_2.url
                bot.send_message(call.message.chat.id, recipe2_url)

bot.polling(none_stop=True)