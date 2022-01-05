dictionary = {
    "name" : "주농",
    "type" : "str",
    "ingredient":["나","나는","해적왕이","될거야"],
    "origin": "코레아"
}

key = input()

if key in dictionary:
    print(dictionary[key])
else:
    print("땡")