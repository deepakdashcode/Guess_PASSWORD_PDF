import os
import shutil
import subprocess
import time
from create_protected import create_password

def create_cpp_file():
    with open('pass.txt') as file:
        password = file.read()
    f = open('structure.cpp')

    ls = f.readlines()
    ls.insert(3, f'int password = {password};')
    f.close()
    f1 = open('guess.cpp', 'w')
    f1.writelines(ls)
# creating number of folders
if os.path.exists('Game'):
    shutil.rmtree('Game')
os.makedirs('Game/')
num = int(input('Enter the number of Students: '))
for i in range(1, num + 1):
    os.makedirs(f'Game/{str(i)}')
    create_password()
    create_cpp_file()
    subprocess.call(["g++", "guess.cpp", '-o', 'guess.exe'])
    # time.sleep(2)
    shutil.copy2('guess.exe', f'Game/{str(i)}')
    shutil.copy2('question.pdf', f'Game/{str(i)}')


    # subprocess.call(['cp', 'a.exe', f'Game/{str(i)}'])
    # subprocess.call(['cp', 'question.pdf', f'Game/{str(i)}'])



