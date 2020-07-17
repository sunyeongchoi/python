# Join() 함수
from builtins import enumerate

colors = ['red', 'yellow', 'green']
result = ','.join(colors)
print(result) #결과 : red,yellow,green

# Split() 함수
langs = 'python,java,c#,sclar'
result = langs.split(',')
print(type(result), result) #결과 : <class 'list'> ['python', 'java', 'c#', 'sclar']
a, b, c, d = langs.split(',') #unpacking(유의사항:갯수맞춰야함)
print(a, b, c, d)

langs = 'python java c# sclar'
result = langs.split() #공백은 구분자 안줘도 됨
print(type(result), result) #결과 : <class 'list'> ['python', 'java', 'c#', 'sclar']

# 일반적인 for loop
my_list = []
for val in range(10):
    if val % 2 == 0:
        my_list.append(val)
print(my_list) #결과 : [0, 2, 4, 6, 8]

# 1. List Comprehensions(포괄적인 리스트)
my_list2 = [val for val in range(10) if val % 2 == 0]
print(my_list2) #결과 : [0, 2, 4, 6, 8]

my_list3 = [val if val % 2 == 0 else 10 for val in range(10)]
print(my_list3) #결과 : [0, 10, 2, 10, 4, 10, 6, 10, 8, 10]

# 2. 문자열 타입 List Comprehension
word1 = 'Hello'
word2 = 'World'
# for i in word1:
#     for j in word2:
#         print(i+j)
my_list4 = [i+j for i in word1 for j in word2]
print(my_list4, len(my_list4)) # 결과 : ['HW', 'Ho', 'Hr', 'Hl', 'Hd', 'eW', 'eo', 'er', 'el', 'ed', 'lW', 'lo', 'lr', 'll', 'ld', 'lW', 'lo', 'lr', 'll', 'ld', 'oW', 'oo', 'or', 'ol', 'od']

my_list5 = [i+j for i in word1 for j in word2 if i != j]
print(my_list5, len(my_list5)) # 결과 : ['ll', 'll', 'oo']

words = 'Yesterday love was such an easy game to play'.split()
print(words) #['Yesterday', 'love', 'was', 'such', 'an', 'easy', 'game', 'to', 'play']


# 일반적 방법
result_list = []
for w in words:
    word_list = [w.upper(), w.lower(), len(w)]
    result_list.append(word_list)
print(result_list) # 결과 : [['YESTERDAY', 'yesterday', 9], ['LOVE', 'love', 4], ['WAS', 'was', 3], ['SUCH', 'such', 4], ['AN', 'an', 2], ['EASY', 'easy', 4], ['GAME', 'game', 4], ['TO', 'to', 2], ['PLAY', 'play', 4]]

# 2차원 배열 형 List Comprehensions
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff) # 결과 : [['YESTERDAY', 'yesterday', 9], ['LOVE', 'love', 4], ['WAS', 'was', 3], ['SUCH', 'such', 4], ['AN', 'an', 2], ['EASY', 'easy', 4], ['GAME', 'game', 4], ['TO', 'to', 2], ['PLAY', 'play', 4]]

for i in stuff:
    print(i)

case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'F']

result = [i+j for i in case_1 for j in case_2]
print(result)

result = [[i+j for i in case_1] for j in case_2]
print(result)

# indexed traversal
langs_list = 'python java c# sclar'.split()

# Bad
for idx in range(len(langs_list)):
    print(f'idx = {idx}, values = {langs_list[idx]}')

# Good - enumerable() 함수
for idx, lang in enumerate(langs_list):
    print(f'idx = {idx}, values = {lang}')

'''
결과 : 
idx = 0, values = python
idx = 1, values = java
idx = 2, values = c#
idx = 3, values = sclar
'''

print(enumerate(langs_list))
print(list(enumerate(langs_list)))

# Dict Comprehensions
my_dict = {idx:val.capitalize() for idx,val in enumerate('Yesterday love was such an easy game to play'.split())}
print(my_dict)
#결과 : {0: 'Yesterday', 1: 'love', 2: 'was', 3: 'such', 4: 'an', 5: 'easy', 6: 'game', 7: 'to', 8: 'play'}

print(dict(enumerate(langs_list)))

# Variable Exchange
a = 10
b = 20
tmp = a
a = b
b = tmp
print(a, b) #결과 : 20 10

# good
a = 10
b = 20
a, b = b, a
print(a, b) # 결과 : 20 10

# Sequence Unpacking
a, *rest = [1, 2, 3]
print(a, type(rest), rest) # 결과 : 1 <class 'list'> [2, 3]

a, *middle, c = [1, 2, 3, 4]
print(a, middle, c) # 결과 : 1 [2, 3] 4

# Judgement T, F
# Bad
attr = True
if attr == True:
    pass
# Good
if attr:
    pass

# Bad
attr = None
if attr == None:
    pass
# Good
if attr is None:
    pass

# zip() 함수
a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c) #(1, 10, 100) (2, 20, 200) (3, 30, 300)

for val in zip((1, 2, 3), (10, 20, 30), (100, 200, 300)):
    print(val)
'''
(1, 10, 100)
(2, 20, 200)
(3, 30, 300)
'''

# index가 같은 값을 tupple로 믂어서 합을 계산하고 List에 저장함
sum_list = [sum(val) for val in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
print(sum_list) #[111, 222, 333]

# Enumerate & Zip
a_list = ['a1', 'a2', 'a3']
b_list = ['b1', 'b2', 'b3']
for i, (a, b) in enumerate(zip(a_list, b_list)):
    print(i, a, b)
'''
0 a1 b1
1 a2 b2
2 a3 b3
'''








