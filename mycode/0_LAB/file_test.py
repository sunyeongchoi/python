import os
import random
import datetime

# log 디렉토리가 없으면 log 디렉토리 생성
if not os.path.isdir('log'):
    os.mkdir('log')

with open('log/count_log.txt', 'a', encoding= 'utf-8') as f:
    for i in range(1, 11):
        stamp = str(datetime.datetime.now())
        value = random.random() * 100000
        f.write(f'stamp : {stamp}, value : {value}\n')
