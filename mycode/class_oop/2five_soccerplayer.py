# 2차원 리스트를 사용해서 5명의 player 정보를 저장하기
names = ['둘리', '길동', '지성', '홍민', '병근']
positions = ['MF', 'DF', 'cf', 'WF', 'GK']
back_numbers = [10, 15, 20, 30, 1]

# zip 함수
for na, po, nu in zip(names, positions, back_numbers):
    print(na, po, nu)
'''
둘리 MF 10
길동 DF 15
지성 cf 20
홍민 WF 30
병근 GK 1
'''

player = [[na, po, nu] for na, po, nu in zip(names, positions, back_numbers)]
print(player)#[['둘리', 'MF', 10], ['길동', 'DF', 15], ['지성', 'cf', 20], ['홍민', 'WF', 30], ['병근', 'GK', 1]]

# SoccerPlayer 클래스 import
from mycode.class_oop.soccer_player import SoccerPlayer

player1 = SoccerPlayer('수녕', 'king', '716')
print(player1)#My Name is 수녕, I play in king
player1.change(7160)
#선수의 등번호를 변경합니다. From716 To 7160
print('----------------------')

players_object = [SoccerPlayer(na, po, nu) for na, po, nu in zip(names, positions, back_numbers)]
print(players_object) #[<mycode.class_oop.soccer_player.SoccerPlayer object at 0x000001E646D1E248>, <mycode.class_oop.soccer_player.SoccerPlayer object at 0x000001E646D1E288>, <mycode.class_oop.soccer_player.SoccerPlayer object at 0x000001E646D1E2C8>, <mycode.class_oop.soccer_player.SoccerPlayer object at 0x000001E646D1E308>, <mycode.class_oop.soccer_player.SoccerPlayer object at 0x000001E646D1E348>]
son = players_object[3]
print(son) #My Name is 홍민, I play in WF
son.name = '호호호'
print(son) #My Name is 호호호, I play in WF
