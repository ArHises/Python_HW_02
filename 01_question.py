"""
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть

5 -> 1 0 1 1 0
2

"""
import random

n = int(input('Enter number of coins: '))

def first_way(n):
    tail_num = random.randint(1 , n - 1)
    coat_of_arms = n - tail_num

    print(f'tails: {tail_num}')
    print(f'coat of arms: {coat_of_arms}')

    if tail_num >= coat_of_arms:
        print(f'flip all coat of arms: {coat_of_arms}')
    else:
        print(f'flip all tails: {tail_num}')

# first_way(n)

def second_way(n):
    tail_num = 0
    coat_of_arms = 0
    print(('enter 0 for tail or 1 for coat of arms: '))
    for i in range(0 , n):
        a = int(input())
        if a == 0:
            tail_num += 1
        else:
            coat_of_arms += 1

    if tail_num >= coat_of_arms:
        print(f'flip all coat of arms: {coat_of_arms}')
    else:
        print(f'flip all tails: {tail_num}')

second_way(n)


