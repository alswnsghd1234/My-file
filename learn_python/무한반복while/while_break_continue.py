numbers = [ 5 ,10 ,15, 20, 25]

for number in numbers:
    # number가 10 보다 작으면 다음 반복으로 넘어갑니다.
    if number <10:
        continue
    print(number)

#반복을 돌린다
for number in numbers:
    #반복대상을 한정하는 방법
    if number >= 10:
        #문장
        #문장
        print("10")


for number in numbers:
    #반복 대상에서 제외하는 방법
    if number < 10:
        continue
