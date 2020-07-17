# 평균을 계산하는 함수를 정의
def my_average(numbers):
    # local variable
    total = 0
    for num in numbers:
        total += num
    my_avg = total / len(numbers)
    return my_avg


def connect(server, port):
    #pass # 함수는 선언했지만 구현내용을 나중에 하고싶은 경우 pass 키워드 사용 (구현 안할 경우 컴파일 에러)
    return 'https://{}:{}'.format(server, port)

def times(n1 = 10, n2 = 20):
    return n1*n2

# *p - tuple type parameter, 아규먼트의 갯수가 가변적
def var_param(*p):
    return p

# **p - dict type parameter
def var_param_dict(**p):
    return p

def tuple_dict_param(n1, n2, *n3, **n4):
    print(n1, n2, sum(n3))
    print(n4)

# 다중 값을 리턴하는 함수
def swap(a, b):
    return b, a


def main():
    prices = [1000, 3000, 2500, 450]
    result = my_average(prices)
    print(result) #결과 : 1737.5

    result2 = connect('server.com', '9080')
    print(result2) #결과 : https://server.com:9080
    result2 = connect(port='8087', server='aa.com')
    print(result2) #결과 : https://aa.com:8087

    result3 = times()
    print(result3) #결과 : 200
    result3 = times(2)
    print(result3) #결과 : 40
    result3 = times(3, 4)
    print(result3) #결과 : 12

    result4 = var_param(1,2,3,4,2,4,)
    print(type(result4), result4) #결과 : <class 'tuple'> (1, 2, 3, 4, 2, 4)

    result5 = var_param_dict(a=1, b=2, c=90)
    print(type(result5), result5) #결과 : <class 'dict'> {'a': 1, 'b': 2, 'c': 90}

    tuple_dict_param(1, 2, 3, 4, 5, 6, 7, a=23, b=45) #결과 : 1 2 25 {'a': 23, 'b': 45}

    result6 = swap(1, 2)
    print(type(result6), result6) #결과 : <class 'tuple'> (2, 1)
    x, y = result6
    print(x, y) #결과 : 2 1


main()

# 함수 외부에서는 로컬변수를 사용할 수 없음
# print(total)

