import random

def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount+1), amount))
    #random.sample(lista[], ile)

choose_random_numbers(6,49)
