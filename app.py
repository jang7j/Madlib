import random
def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = input(f'Guess a number between 1 and {x}')
        if guess < random_num:
            print('sorry guess again. too low')
        else guess > random_num:
        p
guess(10)
