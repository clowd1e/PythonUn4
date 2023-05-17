# import math
#
# N = 30
# for x in range(1, N):
#     for y in range(x, N):
#         z = math.sqrt(x**2+y**2)
#         if z%1 == 0 and x < 30:
#             print(x, y, int(z))

# n = int(input("Podaj iloszcz: "))
#
# suma = 1
#
# for i in range(2, n + 1):
#     if i % 2 == 0:
#         suma += i
#     elif i % 2 != 0:
#         suma -= i
#
# print(suma)

# import random
#
#
# def generujListe(x):
#     tablica = []
#     for i in range(x):
#         a = random.randint(1, 10)
#         tablica.append(a)
#     return tablica
#
#
# def mostElement(tab):
#     maximum = 0
#     liczba = 0
#     for i in tab:
#         if maximum < tab.count(i):
#             maximum = tab.count(i)
#             liczba = i
#
#     print(maximum, liczba)
#
#
# x = int(input("podaj x: "))
# tablica_glowna = generujListe(x)
# print(tablica_glowna)
# z = generujListe(x)
# print(z)
# mostElement(tablica_glowna)
# mostElement(z)

import random

names = ["Jan", "Magda", "Karolinka"]
surnames = ["Kowalski", "Pych", "Kowal"]

def zapelniacz(n):
   list = []
   for i in range(n):
       wiek = random.randint(18, 70)
       tel = random.randint(5000000, 8000000)
       list.append({"name": names[random.randint(0, len(names) - 1)], "surname": surnames[random.randint(0, len(surnames) - 1)], "age": wiek, "phone": tel})
   return list

def wypisywacz(tab):
   for i in tab:
       print(i)

def szukaj(s, tab):
   for i in tab:
       for j in i.keys():
           if s == str(i[j]).lower():
               print(i, i.keys())


tablica = zapelniacz(10)
wypisywacz(tablica)
szukaj(input("Szukaj: "), tablica)