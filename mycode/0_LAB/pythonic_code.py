# join() 함수 : list -> str
colors = ['red', 'yellow','green']
result = ' '.join(colors)
print(result)
result = '/'.join(colors)
print(result)

# split() 함수 : str -> list
langs = 'python,java,c#,sclar'
result = langs.split(',')
print(type(result), result)
a,b,c,d = langs.split(',')
print(a,b,c)

langs = 'python java c# sclar'
# 공백으로 구분하는 문자열인 경우에는
# split() 함수에서 구분자를 주지 않아도 된다.
result = langs.split()
print(result)

# 일반적인 for loop
my_list = []
for val in range(10):
    if val % 2 == 0:
        my_list.append(val)
print(my_list)

# 1. List Comprehension (포괄적인 리스트)
my_list2 = [val for val in range(10)]
print(my_list2)

my_list3 = [val for val in range(10) if val % 2 == 0]
print(my_list3)

my_list4 = [val if val % 2 == 0 else 10 for val in range(10)]
print(my_list4)

# 2. 문자열 타입 list comprehension
word1 = 'Hello'
word2 = 'World'
# for i in word1:
#     for j in word2:
#         print(i+j)
my_list5 = [i+j for i in word1 for j in word2]
print(my_list5, len(my_list5))

my_list = [i+j for i in word1 for j in word2 if i != j]
print(my_list, len(my_list))

words = 'Yesterday love was such an easy game to play'.split()
#print(words)

word_lists = []
for w in words:
    word_list = [w.upper(), w.lower(), len(w)]
    word_lists.append(word_list)
#print(word_lists)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

for word_list in stuff:
    print(word_list)



