# задача 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# F1 = не (Х или Y или Z) 
# F2 = не X и не Y и не Z

# X Y Z  F1 F2
# 0 0 0  1  1
# 0 0 1  0  0
# 0 1 0  0  0
# 0 1 1  0  0
# 1 0 0  0  0
# 1 0 1  0  0
# 1 1 0  0  0
# 1 1 1  0  0


X = bool(input("Enter X: "))
Y = bool(input("Enter Y: "))
Z = bool(input("Enter Z: "))

F1 = not(X or Y or Z)
F2 = not X and not Y and not Z

if F1==F2:
    print("The statment is true")
elif F1!=F2:
    print("The statment is false")




