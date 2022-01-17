"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

def flatten(lst):
    if bool(lst) == False:
        return lst
 
    if isinstance(lst[0], list):
        return flatten(*lst[:1]) + flatten(lst[1:])
 
    return lst[:1] + flatten(lst[1:])

"""
    TESTING
"""

print("TEST1\n", end="\n")

testArr1Initial = [[1,2,[3],4],[[[5]],6],7,8]

print("Test1 > Initial state of the array: ", testArr1Initial)

testArr1Result  = flatten(testArr1Initial)

print("Test1 > Latest status of the array: ", testArr1Result)

print("\nTEST2\n", end="\n")

testArr2Initial = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print("Test2 > Initial state of the array: ", testArr2Initial)

testArr2Result  = flatten(testArr2Initial)

print("Test2 > Latest status of the array: ", testArr2Result)

def reverse(lst):
    lst.reverse()

    for item in lst:
        if isinstance(item, list):
            for sublist in item:
                if isinstance(sublist, list):
                    sublist.reverse()
            item.reverse()

    return lst

"""
    TESTING
"""

print("TEST1\n", end="\n")

testArr1Initial = [[1, 4, [4,2]], [3, 4], [5, 6, 7]]

print("Test1 > Initial state of the array: ", testArr1Initial)

testArr1Result  = reverse(testArr1Initial)

print("Test1 > Latest status of the array: ", testArr1Result)

print("\nTEST2\n", end="\n")

testArr2Initial = [[1, 2], [3, 4], [5, 6, 7]]

print("Test2 > Initial state of the array: ", testArr2Initial)

testArr2Result  = reverse(testArr2Initial)

print("Test2 > Latest status of the array: ", testArr2Result)