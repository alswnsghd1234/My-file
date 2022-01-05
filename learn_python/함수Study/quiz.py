
def std_weight(height, gender):
    if gender == "m":
        std = height * height * 22
        std = round(std / pow(10,4), 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height,std))
    else:
        std = height * height * 21
        std = round(std / pow(10,4), 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height,std))


std_weight(178,"m")

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = std_weight(height / 100 , gender)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))