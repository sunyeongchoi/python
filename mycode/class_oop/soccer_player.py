# SoccerPlayer 클래스 선언
class SoccerPlayer(object):
    # 생성자 선언 - 객체가 생성될 때 호출되는 메서드
    def __init__(self, name, position, back_number):
        # access modifier가 public이라고 볼 수 있음
        self.name = name
        self.position = position
        self.back_number = back_number

    # 일반함수 (instance method), back_number값을 입력받아변경하는 함수
    # 함수의 첫번째 파라미텅 self가 있어야 클래스에ㅔ 속한 함수가 된다.
    # 첫번째 파라미터의 이름은 self가 아니어도 괜찮음
    def change(self, new_number):
        print(f'선수의 등번호를 변경합니다. From{self.back_number} To {new_number}')
        self.back_number = new_number


    # toString() 메서드와 동일한 역할
    # 객체와 주소가 아니라 객체가 가진 특정 인스턴스 값을 출력
    def __str__(self):
        return f'My Name is {self.name}, I play in {self.position}'

def main():
    # 객체 생성
    dooly = SoccerPlayer('둘리', 'MF', 10)
    # __str__가 있을 경우 자동으로 사용됨
    print(dooly) # My Name is 둘리, I play in MF
    print('현재 선수의 등번호는 {}'.format(dooly.back_number))#현재 선수의 등번호는 10
    dooly.change(99)
    print('변경된 선수의 등번호는 {}'.format(dooly.back_number))#변경된 선수의 등번호는 99

