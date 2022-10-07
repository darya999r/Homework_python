# задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def listPrimeMultipliers (N):
    arrayPrimeNumbers = [2, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    array = []
    
    if N==0: print("Number has no prime multipliers!")
    elif N!=1 and N!=0:
        for i in range(len(arrayPrimeNumbers)):
            while N%arrayPrimeNumbers[i]==0:
                array.append(arrayPrimeNumbers[i])
                N//=arrayPrimeNumbers[i]
        return array
    else: print("Number has no prime multipliers!")
    
try:
    n = int(input("Enter number N: "))
    print(listPrimeMultipliers(n))
except:
    print("Input error!")


