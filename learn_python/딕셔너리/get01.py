dictionary = {
    "name" : "주농",
    "type" : "str",
    "ingredient":["나","나는","해적왕이","될거야"],
    "origin": "코레아"
}

#존재하지 않는 키에 접근해 봅니다.
value = dictionary.get("존재하지않는키")
print(value)

#None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다")