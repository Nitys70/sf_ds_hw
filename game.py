# Игра угадай число 
import numpy as np

number = np.random.randint(0,101)
count = 0

while True:
    count+=1
    predict_num=int(input('Угадай число от 0 до 100: '))
    if predict_num > number:
        print('Число должно быть меньше')
    
    elif predict_num < number:
        print('Число должно быть больше')
    
    else:
        print(f'Поздравляю, вы угадали за {count} попыток! Верный ответ - число {number}')
        break
    

