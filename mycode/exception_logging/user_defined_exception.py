# 사용자 정의 Exception 클래스
# 음수 값이 입력되었을 때 강제로 예외를 발생기키기
class NegativePriceException(Exception):
    def __init__(self):
        print('Price can\'t be Negative')
        raise AttributeError

def calc_price(value):
    price = value + 100
    if price < 0:
        raise NegativePriceException
    return price

#result = calc_price(100)
#print(result) #1100
result = calc_price(-101)
print(result) #Price can't be Negative
