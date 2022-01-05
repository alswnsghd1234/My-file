#컴퓨터 속도 비교 할 때 사용하면 괜찮다.
#다른 곳에도 사용할 수 있는지 봐야겠다.


import time

number = 0

#time.time()은 유닉스 타임이란 사계 표준시로, 1970년 1월 1일 0시0분0초를 기준으로
#몇 초가 지났는지 정수로 나타낸것이다.

target_tick = time.time() + 5
while time.time() < target_tick:
    number +=1

print("5초동안 {}번 반복했습니다".format(number))