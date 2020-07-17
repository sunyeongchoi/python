# mode 설정하지 않으면 default가 r (read)
# myfile = open('i_have_a_dream.txt')
# contents = myfile.read()
# print(contents)
# myfile.close()


# with 구문 사용
with open('i_have_a_dream.txt') as my_file:
    content = my_file.read()
    word_list = content.split(' ')
    line_list = content.split('\n')

print('Total Number of characters', len(content))
print('Total Number of word', len(word_list))
print('Total Number of line', len(line_list))
