
# won = input('원화 금액')
# dollar = input('환율 금액')

# try:
#     print(int(won)/int(dollar))
# except:
#     print('예외발생')
# print('ㅎㅎ')

#에러 만들기 코드

class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력 불가")
        
try:
    num = int(input("음수를 입력해 주쇼"))
    if num >= 0:
        raise PositiveNumberError("양수는 입력 불가")
except PositiveNumberError as e:
    print("에러 발생", e)