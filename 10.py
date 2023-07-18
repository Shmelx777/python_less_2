# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random
while True:
    n = int(input("Введите кол-во монеток: "))
    if n > 0: 
        break
arrCoins = []
i = 0
tempGerb = 0
tempReshka = 0
while i != n:
    i += 1
    arrCoins.append(random.randint(0,1))

print(arrCoins)

for s in range(len(arrCoins)):
    if(arrCoins[s] == 0):
        tempGerb += 1
    else:
        tempReshka += 1

if(tempGerb < tempReshka):
    print(f"Минимальное количество монет с гербом, нужно перевернуть - {tempGerb}")
elif(tempGerb > tempReshka):
     print(f"Минимальное количество монет с решкой, нужно перевернуть - {tempReshka}")
else: 
     print(f"Количество одинаковое, можно перевернуть любые - {tempGerb}")