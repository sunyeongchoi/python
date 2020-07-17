books = list()
books.append({'제목':'개발자의 코드', '출판연도':'2013.02.28', '출판사':'A출판','쪽수':200,'추천유무':False})
books.append({'제목':'클린 코드', '출판연도':'2013.03.04', '출판사':'B출판','쪽수':584,'추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014.07.02', '출판사':'A출판','쪽수':296,'추천유무':True})
books.append({'제목':'구글드', '출판연도':'2010.02.10', '출판사':'B출판','쪽수':526,'추천유무':False})
books.append({'제목':'강의력', '출판연도':'2013.12.12', '출판사':'C출판','쪽수':248,'추천유무':True})

print(books)

# 일반적 방법
# 250쪽 넘는 책 목록 만들기
pages_list = []
idx = 0
for book in books:
    pages = book['쪽수']
    if pages > 250:
        pages_list.append(books[idx])
        idx += 1
    else:
        idx += 1
print(pages_list)
'''
결과 :
[{'제목': '클린 코드', '출판연도': '2013.03.04', '출판사': 'B출판', '쪽수': 584, '추천유무': True}, {'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A출판', '쪽수': 296, '추천유무': True}, {'제목': '구글드', '출판연도': '2010.02.10', '출판사': 'B출판', '쪽수': 526, '추천유무': False}]
'''



# 추천유무가 True인 책 목록 만들기
recomm_list = []
idx = 0
for book in books:
    recomm_exist = book['추천유무']
    if recomm_exist is True:
        recomm_list.append(books[idx])
        idx += 1
    else:
        idx += 1
print(recomm_list)
'''
결과 :
[{'제목': '클린 코드', '출판연도': '2013.03.04', '출판사': 'B출판', '쪽수': 584, '추천유무': True}, {'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A출판', '쪽수': 296, '추천유무': True}, {'제목': '강의력', '출판연도': '2013.12.12', '출판사': 'C출판', '쪽수': 248, '추천유무': True}]
'''

# 출판사 목록 만들기
title_list = []
pub_com = set()
for book in books:
    publish = book['출판사']
    title_list.append(publish)
    pub_com = set(title_list)
print(pub_com)
'''
결과 : 
{'B출판', 'A출판', 'C출판'}
'''


# list comprehensions
# 출판사 목록 만들기
pub_com = set([book['출판사'] for book in books])
print(pub_com)

# 추천유무가 True인 책 목록 만들기
recomm_exist = [book['제목'] for book in books if book['추천유무'] is True]
print(recomm_exist)

# 250쪽 넘는 책 목록 만들기
pages_list = [book['제목'] for book in books if book['쪽수'] > 250]
print(pages_list)

# 모든 쪽수의 합
all_pages = []
all_pages = sum(book['쪽수'] for book in books)
print(all_pages)
