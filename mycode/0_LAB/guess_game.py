import random

print('1~100까지의 아무 숫자나 입력해줏요~!')
# 1~100까지의 랜덤 숫자
guess_number = random.randint(1, 100)

# 사용자로부터 숫자 입력받기
user_number = int(input())

# 랜덤 숫자와 입력받은 숫자가 같으면 game 종료
# 정답 알려줌, 몇 번 만에 맞췄는지 알려줌
count = 0
while guess_number != user_number:
    # 입력 받은 숫자 > 랜덤숫자 -> '숫자가 너무 큽니다.'
    # 입력 받은 숫자 < 랜덤숫자 -> '숫자가 너무 작습니다.'
    if user_number > guess_number:
        print('숫자가 너무 큽니다.')
    elif user_number < guess_number:
        print('숫자가 너무 작습니다.')
    count += 1
    user_number = int(input())
else:
    print(f'정답은 {guess_number} 입니다.')
    print(f'당신은 정답을 {count} 번 만에 맞췄습니다.')
