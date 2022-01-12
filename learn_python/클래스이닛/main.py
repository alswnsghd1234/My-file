import os
import csv
from post1 import Post
# 파일 경로
file_paht = "./클래스이닛/data.csv"

# post 객체를 저장할 리스트
post_list = []


# data.csv 파일이 있다면
if os.path.exists(file_paht):
    #게시글 로딩
    print("게시글 로딩중")
    f = open(file_paht, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴트 생성하기
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    f = open(file_paht, "w", encoding="utf8", newline="")
    f.close()
    
    
print(post_list[1].get_title())