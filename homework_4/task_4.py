# задача 4. Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

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

def NOK(arr1, arr2):
    arrA = [elem for elem in arr1 if elem not in arr2]
    arrB = [elem for elem in arr2 if elem not in arr1]
    arrC = []
    k=0
    
    while k<len(arr1):
        for i in range(len(arr2)):
            if arr2[i]==arr1[k]:
                arrC.append(arr2[i])
                if arr2.count(arr2[i])>1:
                    break
        k+=1
    
    arrResult = arrA + arrB + arrC
    print("Total multipliers", arrResult)
    nok = 1
    for d in arrResult:
        nok *= d
    return nok
    
try:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))

    aPrimeMult = listPrimeMultipliers(a)
    bPrimeMult = listPrimeMultipliers(b)
    print("The prime multipliers of numbers a and b: ", aPrimeMult, bPrimeMult)

    res = NOK(aPrimeMult, bPrimeMult)
    print(res)

except:
    print("Input error!")