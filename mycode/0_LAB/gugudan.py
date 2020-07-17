print('구구단 몇 단을 계산할까요(1~9)?')
dan_num = int(input())
while(dan_num is not 0):
    for j in range(10):
        print(f'{dan_num} X {j} = {dan_num*j}')
    print('구구단 몇 단을 계산할까요(1~9)?')
    dan_num = int(input())
else:
    print('구구단 게임을 종료합니다.')