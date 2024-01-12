import random as r

def guess_password(password):
    try:
        n = int(input('Guess the password : '))
        while n != password:
            if n > password:
                print('Lower.')
            else:
                print('higher')
            n = int(input('Guess the password : '))
        print('Correct Guess.')
    except Exception as e:
        print('Invalid integer')

guess_password(543212)
