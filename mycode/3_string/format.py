# 1. %formatting : c언어 스타일
# 2. string format 함수 : {}에 대응하는 값을 format()의 인자로 전달
# 3. f-string : python3.6 이상에서만 사용

temperature = 36
print('1. 온도값은 %d %.2f' % (temperature, temperature))
print('2. 온도값은 {}'.format(temperature))
print(f'3. 온도값은 {temperature}')

print("Art : %5d, Prince per Uint: %8.2f" % (453, 59.058))
print("Art : %d, Prince per Uint: %.2f" % (453, 59.058))

print("Art : {0:5d}, Prince per Unit : {1:8.2f}".format(453, 59.058))
print("Art : {0:d}, Prince per Unit : {1:.2f}".format(453, 59.058))

print("Product: %5s, Prince per unit: %.5f" % ("Apple", 5.243))
print("Product: {0:10s}, Price per unit: {1:10.3f}.".format("Apple", 5.243))
print("Product: {0:>10s}, Price per unit: {1:10.3f}.".format("Apple", 5.243))


print("Product: {name:>10s}, Price per unit: {price:10.3f}.".format(name="APPLE", price=5.243))
