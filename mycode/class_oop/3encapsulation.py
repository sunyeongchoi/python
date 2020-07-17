# Product class 선언
class Product(object):
    # 생성자
    def __init__(self, name):
        # __name이 private 변수
        self.__name = name

    # toString()
    def __str__(self):
        return f'Product의 이름은 {self.__name}'

    # getter
    @property
    def name(self):
        return self.__name

    # setter
    @name.setter
    def name(self, name):
        self.__name = name

# 객체 생성
product = Product('텔레비전')
print(product) #Product의 이름은 텔레비전
# print(product.__name) #AttributeError: 'Product' object has no attribute '__name'
print(product.name) #텔레비전
product.name = '안녕클레오파트라'
print(product) # Product의 이름은 안녕클레오파트라



