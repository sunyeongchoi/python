# abstract method를 가진 부모 클래스 선언
class Animal(object):
    def __init__(self, name):
        self.name = name

    # abstract method
    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof Woof!'
    def pet(self):
        return 'I,m Pet'

my_ani = Animal('동물')
#print(my_ani.name)#동물
#my_ani.talk() #에러 발생

animals = [Cat('고양이'), Dog('강아지1'), Dog('강아지2')]
for ani in animals:
    print(ani.talk())
    '''
    Meow!
    Woof Woof!
    Woof Woof!
    '''
    #print(ani.pet()) #'Cat' object has no attribute 'pet'



