import sys

def say_hello(msg):
    return "Hello" + msg

def main():
    msg = sys.argv[1]
    print(msg)
    if msg is None:
        print('enter msg')
    else:
        print(say_hello(msg))

if __name__=='__main__':
    print('직접실행')
    main()
else:
    print('import 되어 실행됨')

