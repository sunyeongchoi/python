# zip() 함수 사용하기
days = ['월요일', '화요일', '수요일']
coffees = ['아메리카노', '라떼', '바닐라', '녹차']
for day, coffee in zip(days, coffees):
    print(f'{day}에는 {coffee}를 마셔요')

'''
결과 : 
월요일에는 아메리카노를 마셔요
화요일에는 라떼를 마셔요
수요일에는 바닐라를 마셔요
'''
print(zip(days, coffees)) #결과 : <zip object at 0x000001E6C2CA9208>
print(list(zip(days, coffees))) #결과 : [('월요일', '아메리카노'), ('화요일', '라떼'), ('수요일', '바닐라')]
print(dict(zip(days, coffees))) #결과 : {'월요일': '아메리카노', '화요일': '라떼', '수요일': '바닐라'}

