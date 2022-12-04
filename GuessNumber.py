import random
import sys


def inputGuess():
    while True:
        a = input('Guess:')
        try:
            a = int(a)
            return a
        except ValueError:
            print('Enter integer only!')


def guess():
    n = random.randint(0, 100)
    x = True
    b = 0
    print(n)
    while x:
        a = inputGuess()
        b += 1
        if a == n:
            print('Right guess!')
            if b == 1:
                print('Congratulation!You are super lucky!')
            elif 2 <= b <= 5:
                print('Lucky guy!')
            elif 6 <= b <= 10:
                print('Not bad!')
            else:
                print("Uhh...That's OK.")
            x = False
        else:
            print('Wrong!')
            if b <= 15:
                if a < n:
                    print('Try bigger!')
                elif a > n:
                    print('Try smaller!')
            else:
                print('Enough! You are really bad lucky! That number is ', n)
                x = False


y = True
while y:
    guess()
    c = input('One more time?(Y/y for yes, others for no): ')
    if c not in ['Y', 'y']:
        y = False
        print('Bye!')
