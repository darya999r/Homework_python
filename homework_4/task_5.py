# задача 5 необязательная Сделать локальный чат-бот с JSON хранилищем 
# на основе приложенного буткемпа. Тема чат-бота любая. 
# Просьба - постараться не использовать простой одномерный список.

from random import *
import json

recipes = []

def save():
    with open('recipes.json', 'w', encoding='utf-8') as rcp:  
        rcp.write(json.dumps(recipes,ensure_ascii=False)) 
    print('Database saved successfully!')

def load():
    recipes='recipes.json'
    with open(recipes, 'r', encoding='utf-8') as rcp:
        recipes_local = json.load(rcp)
    print('Database loaded successfully!')
    return recipes_local

try:
    load()
except:
    snack = ["salad Caesar", "salad with arugula"]
    first_course = ["pea soup", "borscht"]
    second_course = ["mashed potatoes with cutlet", "pasta with cheese"]
    dessert = ["Napoleon cake", "carrot cake"]
    drinks = ["apple juice", "berry juice"]
    recipes = [snack, first_course, second_course, dessert, drinks]

while True:
    command = input("Enter command: ")
    if command == "/start":
        print("Welcome to the chef-bot!")
    elif command == "/stop":
        print("The chif-bot bids you farewell.\nHopefully it was helpful.\nCome back for new recipes!!!")
        break
    elif command == "/all":
        name_group = input("Enter the name of the group: ")
        if name_group == "snack":
            print("Here is the entire collection of recipes snacks: ")
            print(snack)
        elif name_group == "first_course":
            print("Here is the entire collection of recipes first_courses: ")
            print(first_course)
        elif name_group == "second_course":
            print("Here is the entire collection of recipes second_courses: ")
            print(second_course)
        elif name_group == "dessert":
            print("Here is the entire collection of recipes desserts: ")
            print(dessert)
        elif name_group == "drinks":
            print("Here is the entire collection of recipes drinks: ")
            print(drinks)
        elif name_group == "all":
            print("Here is the entire collection of recipes from the chef-bot: ")
            print(recipes)
    elif command == "/add":
        name_group = input("Enter the name of the group: ")
        if name_group == "snack":
            f = input("Enter the name of the recipe: ")
            snack.append(f)
            print("Recipe added to collection!")
        elif name_group == "first_course":
            f = input("Enter the name of the recipe: ")
            first_course.append(f)
            print("Recipe added to collection!")
        elif name_group == "second_course":
            f = input("Enter the name of the recipe: ")
            second_course.append(f)
            print("Recipe added to collection!")
        elif name_group == "dessert":
            f = input("Enter the name of the recipe: ")
            dessert.append(f)
            print("Recipe added to collection!")
        elif name_group == "drinks":
            f = input("Enter the name of the recipe: ")
            drinks.append(f)
            print("Recipe added to collection!")
        elif name_group == "new_group":
            f = []
            f = input("Enter the name of the recipe: ")
            recipes.append(f)
            print("Recipe group added to the collection!")
        else: print("Input error!")
    elif command == "/del":
        name_group = input("Enter the name of the group: ")
        if name_group == "snack":
            f = input("Enter the name of the recipe: ")
            try:
                snack.remove(f)
                print("The recipe was successfully removed from the collection!")
            except: print("Such a recipe is not in the cillection!")
        elif name_group == "first_course":
            f = input("Enter the name of the recipe: ")
            try:
                first_course.remove(f)
                print("The recipe was successfully removed from the collection!")
            except: print("Such a recipe is not in the cillection!")
        elif name_group == "second_course":
            f = input("Enter the name of the recipe: ")
            try:
                second_course.remove(f)
                print("The recipe was successfully removed from the collection!")
            except: print("Such a recipe is not in the cillection!")
        elif name_group == "dessert":
            f = input("Enter the name of the recipe: ")
            try:
                dessert.remove(f)
                print("The recipe was successfully removed from the collection!")
            except: print("Such a recipe is not in the cillection!")
        elif name_group == "drinks":
            f = input("Enter the name of the recipe: ")
            try:
                drinks.remove(f)
                print("The recipe was successfully removed from the collection!")
            except: print("Such a recipe is not in the cillection!")
        elif name_group == "group":
            f = input("Enter the name of the group: ")
            try:
                recipes.remove(f)
                print("The group was successfully removed from the collection!")
            except: print("Such a group is not in the cillection!")
        else: print("Input error!")
    elif command == "/random":
        name_group = input("Enter the name of the group: ")
        if name_group == "snack":
            print("Here's your random recipe: " + choice(snack))
        elif name_group == "first_course":
            print("Here's your random recipe: " + choice(first_course))
        elif name_group == "second_course":
            print("Here's your random recipe: " + choice(second_course))
        elif name_group == "dessert":
            print("Here's your random recipe: " + choice(dessert))
        elif name_group == "drinks":
            print("Here's your random recipe: " + choice(drinks))
        else: print("Input error!")
    elif command == "/help":
        print("There's some help here)))")
    elif command == "/save":
        save()
    elif command == "/load":
        recipes_local = load()
        print(recipes_local)
    else: print("No such command exists!!!\nFor help enter /help")
    