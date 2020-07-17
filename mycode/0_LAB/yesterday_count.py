'''
yesterday.txt 파일을 읽어서
'YESTERDAY', 'yesterday', 'Yesterday 단어가 몇 번 나오는지 Counting 해보기'
'''

# file open
# mode : r(read), w(write), a(append)
# 이미지 등 파일 읽을 때 : rb(read binary), wb(write Binary)
file = open('yesterday.txt', 'r')
# file의 내용을 읽은 값을 저장한 변수
yesterday_lyric = ''
while 1:
    line = file.readline()
    if not line:
        break
    yesterday_lyric += line.strip() + '\n'

print(yesterday_lyric)

print(len(yesterday_lyric))

n_of_YESTERDAY = yesterday_lyric.upper().count('YESTERDAY')
print(n_of_YESTERDAY)
n_of_yesterday = yesterday_lyric.lower().count('yesterday')
print(n_of_yesterday)
n_of_Yesterday = yesterday_lyric.count('Yesterday')
print(n_of_Yesterday)

file.close()

