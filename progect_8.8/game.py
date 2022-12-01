"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

count = 0 # количество попыток
max = 100 # максимальное число
min = 1 # минимальное число

while True:
    count+=1
    predict_number = (max + min) // 2
    
    if predict_number > number:
        max = predict_number

    elif predict_number < number:
        min = predict_number
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла