# Stack - LIFO
my_stack = [20, 10, 30, 40, 20]
print(my_stack)
my_stack.append(100)
print(my_stack)
print(my_stack.pop())

#입력 : 1 2 3 4 5
#출력 : 5 4 3 2 1
#word = input("Input a word : ")
#word_list = list(word)
#for i in range(len(word_list)):
#    print(word_list.pop())

# Queue - FIFO
my_stack.pop(0)
print(my_stack)
my_stack.append(30)
print(my_stack)

# Tuple
print(my_stack)
my_stack.append(30)
print(set(my_stack))

my_tuple = tuple(my_stack)
print(type(my_tuple), my_tuple)
# my_tuple[0] = 50
print(my_tuple * 2)
print(len(my_tuple))

my_int = (1)
print(type(my_int), my_int)
my_tuple2 = (1,)
print(type(my_tuple2), my_tuple2)

# Set
my_set = set([40, 20, 49, 50, 20, 50])
print(my_set)
my_set.add(49)
print(my_set) #이미 49가 있기 때문에 무시됨
my_set.remove(49)
print(my_set)
my_set.discard(20)
print(my_set)
my_set.discard(10)
print(my_set)
#my_set.remove(10)
#print(my_set)

s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])
print(s1.union(s2)) #합집합
print(s1.intersection(s2)) #교집합
print(s2-s1) #차집합

# Dict
my_dict = {} #Dict생성방법1
my_dict2 = dict() #Dict생성방법2
print(type(my_dict), type(my_dict2))

my_dict['java'] ='자바'
my_dict['python'] = '파이썬'
my_dict['javascript'] = '자바스크립트'
print(my_dict)
print(my_dict['java'])
#print(my_dict['python1']) #매칭되는 key값이 없으면 KeyError발생
print(my_dict.get('python1')) #매칭되는 key값이 없으면 None 반환

# None반환을 통해 조건문 사용
value = my_dict.get('python1')
if value :
    print(value)
else:
    print('해당 key가 존재하지 않습니다')

# 해당 키 삭제
del my_dict['python']
print(my_dict)

# in 구문을 사용해서 해당 key 있는지를 체크
print('java' in my_dict)

# Keys(), values(), items()
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items()) #튜플 형태로 반환

# setdefault() 함수
print(my_dict) # 결과 : {'java': '자바', 'javascript': '자바스크립트'}
my_dict.setdefault('python', '파이썬')
print(my_dict) # 결과 : {'java': '자바', 'javascript': '자바스크립트', 'python': '파이썬'}
my_dict.setdefault('python', '추가될까?')
print(my_dict) # 결과 : {'java': '자바', 'javascript': '자바스크립트', 'python': '파이썬'}