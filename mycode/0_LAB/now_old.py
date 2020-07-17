from datetime import datetime as dt

nowyear = dt.today().year
print('당신이 태어난 년도를 입력해주세요')
born_year = int(input())
old = nowyear - born_year + 1
if 17 <= old < 20:
    print('당신은 고등학생 입니다.')
elif 20 <= old < 27:
    print('당신은 대학생 입니다.')
else: print('당신은 학생이 아닙니다.')
