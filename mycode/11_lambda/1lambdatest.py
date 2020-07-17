# 일반적인 함수 정의
def add(x,y):
    return x + y
print(add(10,20))

# lambda 함수 정의
add2 = lambda x, y: x + y
print(add2(10, 20))

# 제곱승, 곱하기, 나누기 람다함수를 정의해서 호출
my_pow = lambda x, y: x ** y
print(my_pow(2, 3))

my_pow = lambda x: x ** 2
print(my_pow(2)) #4
print((lambda x: x ** 2)(3)) #9

my_div = lambda x: x / 2
print(my_div(10))

# Map() 함수
my_arr = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, my_arr)
print(result)#<map object at 0x00000243D8449C48>
print(list(result))#[2, 4, 6, 8, 10]

result = list(map(lambda x: x*2, my_arr))
print(result)#[2, 4, 6, 8, 10]

# [1, 2, 3, 4, 5] + [1, 2, 3, 4, 5]
# add(1, 1) add(2, 2) add(3, 3)....

f_add = lambda x, y: x + y
print(f_add(1, 1))#2

result = list(map(f_add, my_arr, my_arr))
print(result)#[2, 4, 6, 8, 10]

# my_arr 리스트의 값을 제곱승 해서 다른 리스트에 저장하세요
# lambda 함수와 map() 함수 사용합니다.
result = list(map(lambda x: x**2, my_arr))
print(result) #[1, 4, 9, 16, 25]

# 값을 차례로 한개씩 가져오는 함수 -> list안에서는 동작 안함
f_pow = lambda x: x**2
result = map(f_pow, my_arr)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Filter 함수
result = filter(lambda x: x > 2, my_arr)
print(result) #<filter object at 0x000001C210DCD308>
print(list(result)) #[3, 4, 5]

for val in filter(lambda x: x > 2, my_arr):
    print(val) # 3 4 5

# reduce 함수
# functools.py 라는 모듈안에 있는 reduce 함수를 불러오기
from functools import reduce
result = reduce(lambda x, y: x + y, my_arr)
print(result) #15



