list_a = [0,1,2,3,4,5]

del list_a[1]
print(list_a)

list_a.pop(2)
print(list_a)

#pop 함수의 매개변수에 아무 것도 입력하지 않으면 자동으로 -1이 들어가는 것으로
# 취급해서 마지막 요소를 제거합니다.

#del 함수는 인덱스로 리스트 요소 제거

list_b = [1,2,3,4,5]
del list_b[3:6]
print(list_b)

#remove() 함수는 괄호안에 있는 값을 리스트 요소에서 제거

list_c = [1,2,3,4,5]
list_c.remove(2)
print(list_c)

#clear() 함수는 리스안에 전부 제거
list_d = [1,2,3,4,5]
list_d.clear()
print(list_d)