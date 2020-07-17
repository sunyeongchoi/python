from mycode import using_converter
# 2. 모듈명을 import하면서 alias 설정하기
from mycode import using_converter as conv
# 3. 모듈에 속한 함수만 import하기
from mycode.using_converter import convert_c_to_f
# 4. 모듈에 속한 모든 함수 import하기
from mycode.using_converter import *

# 연습문제
print('섭씨 온도를 입력해주세요')
temperature = float(input())
# 1. 모듈명.convert_c_to_f() 함수 호출
fah = using_converter.convert_c_to_f(temperature)
print('섭씨온도 : ', temperature)
print('화씨온도 : ', fah)

# 2. 모듈명을 import하면서 alias 설정하기
fah = conv.convert_c_to_f(temperature)
print('섭씨온도 : ', temperature)
print('화씨온도 : ', fah)

# 3. import된

# 4. 





# # 소수점 둘째자리까지 출력하기
# print('화씨 온도로 변환한 온도는 : {:.2f}'.format(hwasi))


