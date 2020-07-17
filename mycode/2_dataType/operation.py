# 한줄주석
'''
block주석
사칙연산
실행 : ctrl + shift + f10
주석 : 범위잡고(shift + 방향키) + ctrl + /
'''
# 자바에서 + 는 연결 BUT 파이썬 에서는 연산
n1 = 100
n2 = 200
print('n1 = ', n1, n2) # 결과 : n1  = 100 200
print(n1+n2) # 결과 : 300

mystr = 'hello'
mystr2 = "hello"

print(mystr, mystr2) # 결과 : hello hello
print(mystr + mystr2) # 결과 : hellohello

my_float = '76.3'
print(type(my_float))
my_float = float(my_float)
print(type(my_float))

a = 100
b = 100
print(id(a), id(b))

a = "hello"
b = "hello"
print(id(a), id(b))

print(str(n1)+str(n2)) # 결과 : 100200