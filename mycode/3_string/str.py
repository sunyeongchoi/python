# 문자열

greet = 'Hello' * 4 + '\n'
end = 'Goodbye'
print(greet + greet + end)

print("\"I love back slash \"")

flag = True
print(type(flag))
print(type(str(flag)))


# 문자열 인덱스
greeting = 'HELLO WORLD!'
print(greeting[0])
print(greeting[1])
print(greeting[11])
# print(greeting[12])

# 문자열 슬라이싱
print(greeting[0:2])
print(greeting[6:])
print(greeting[:7])
print(greeting[-3:])

print(len(greeting))




word = 'GOOD manufacturing Practice'
print(word)
print(word.upper())

print(word.split(" "))
my_wordlist = word.split(" ")
word_list = list(word)
print(word_list)
str1, str2, str3 = my_wordlist
print(str1)
print(str2)
print(str3)

print(type(word.split(" ")))
print(word.isdigit())
print(word.title())
print(word.startswith('a'))
print(word.startswith('G'))
print(word.count('a'))
print(word.upper().count('a'))
print(word.find('Practice'))
print(word.strip())
print(word.rstrip())
print(word.islower())
print(word.isupper())

# packing
my_list = ['a', 'b', 'c']

# unpacking - 갯수 맞아야 가능
a1, a2, a3 = my_list
print(a1, 'a1')
print(a2)
print(a3)
print(greeting.title())
print(greeting.capitalize())





