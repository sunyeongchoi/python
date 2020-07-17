# try ~ except ~ else
# try ~ except ~ finally

for i in range(10):
    try:
        result = 10 / i
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result) #ZeroDivisionError: division by zero
    finally:
        print('종료되었습니다.')


