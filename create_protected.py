from create import create_pdf
import random as r


def create_password():
    num = r.randint(1, 10000)

    password = str(num)
    create_pdf(password)
    print(password)
    with open('pass.txt', 'w') as f:
        f.write(password)
