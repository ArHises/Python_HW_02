"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.

4 4 -> 2 2
5 6 -> 2 3

"""
# Doing math:

#     first + second = sum
#     first * second = p

#     second = sum - first

#     -first^2 + sum * first = p

#     first^2 - sum * first + p = 0

#     a = 1
#     b = -sum
#     c = p

#     first = (sum + sqrt(sum^2 - 4*p)) / 2
#     second = (sum - sqrt(sum^2 - 4*p)) / 2

import math

sum = int(input('Enter sum: ')) # = first + second
product = int(input('Enter product: ')) # = first * second

def first_way(sum, product):
    first = (sum + math.sqrt(sum**2 - 4*product)) / 2
    second = (sum - math.sqrt(sum**2 - 4*product)) / 2

    print(f'first num: {int(first)} ; second num: {int(second)}')

# first_way(sum, product)

def second_way(sum, product):
    for i in range(sum):
        for j in range(product):
            if sum == i + j and product == i * j:
                print(i, j)
                return

second_way(sum, product)