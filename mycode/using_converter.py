# 섭씨 온도를 화씨 온도로 변환하는 코드
# 1. 모듈명을 import 하기 : from 시작기준은 프로젝트 폴더명 기준이다!!
from mycode import fah_converter
# 2. 모듈명을 import 하면서 alias 명 설정하기
from mycode import fah_converter as conv
# 3. 모듈에 속한 convert_c_to_f 함수만 import 하기
from mycode.fah_converter import convert_c_to_f
# 4. 모듈에 속한 모든 함수 import 하기
from mycode.fah_converter import *

print('변환하고 싶은 섭씨 온도를 입력해 주세요:')
temperature = float(input())
print('섭씨온도 :', temperature)

# 1. 모듈명.convert_c_to_f() 함수 호출
fah = fah_converter.convert_c_to_f(temperature)
# 2. aliasing 된 모듈명.convert_c_to_f() 함수 호출
fah = conv.convert_c_to_f(temperature)
# 3. import 된 convert_c_to_f() 함수 호출
fah = convert_c_to_f(temperature)

# print('화씨온도 :', round(result, 2))
# 소수점 둘째자리까지 출력
print('화씨온도 : {:.2f}'.format(fah))

print(say_hello('Python'))
