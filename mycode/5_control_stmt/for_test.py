import random

# for-in 구문 사용
for val in [0, 1, 2]:
    print(val)

# range(start, end, 증가치)함수
# start의 default값은 0
# end는 exclusive하며, 항상 end -1
# 증가치의 default 값은 1
for val in range(0, 10):
    print(val, end='')

# for -> while 변경
idx = 0
while idx < 10:
    print(idx)
    idx += 1

print('break~~~~~~')
for val in range(10):
    if val == 5:
        break
    print(val)
# 1 2 3 4
print('continue~~~~~~')
for val in range(10):
    if val == 5:
        continue
    print(val)
else:
    print('EOP')
# 1 2 3 4 6 7 8 9
for val in range(0, 10, 2):
    print(val)

favor_hobby = ['finishing', 'reading', 'shopping']
for hobby in favor_hobby:
    print(hobby)

# dict 타입
wish_travel_city = {'bangkok':'Thai',
                    'LA':'USA',
                    'Seoul':'Korea',
                    'bangkok':'ThaiLand'}
print(wish_travel_city)
print(wish_travel_city["LA"]) #USA
print(wish_travel_city["bangkok"]) #ThaiLand --> 같은 키값이 두개 있으면 둘중 어떤 값이 사용될 지 모른다. -> 같은 키값을 사용하면 안된다.

# key와 value를 출력할 때 keys 함수 사용
for city in wish_travel_city.keys():
    print('결과는 : {} in {}'.format(city, wish_travel_city[city]))
'''
결과는 : bangkok in ThaiLand
결과는 : LA in USA
결과는 : Seoul in Korea
'''
# items는 key와 value 둘 다 꺼내옴
for city, country in wish_travel_city.items():
    print(f'{city} in {country}')

for val in range(1, 11):
    ticket = random.randint(1, 100)
    print(f'index{val}: random value {ticket}')




