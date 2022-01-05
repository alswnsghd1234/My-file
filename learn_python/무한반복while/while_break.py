i = 0

while True:
    print("{}번째 반복문이다".format(i))
    i = i + 1

    #반복을 종료한다.
    input_text = input(">종료하시겠습니까?(y/n): ")
    if input_text in ["y" ,"Y"]:
        print("반복을 종료한다")
        break
# i = 0

# while True:
#     print("{}번째 반복이다.".format(i))
#     i = i + 1
#     #반복문 종료
#     input_text = input("반복문종료할거면(y/n) ")
#     if input_text in ["y","Y"]:
#         print("반복문 종료")
#         break