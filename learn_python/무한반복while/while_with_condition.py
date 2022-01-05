#해당하는값 모두 제거하기

list_test = [1,2,3,4,2,2,6]
value = 2

while value in list_test:
    list_test.remove(value)
print(list_test)

list_a = [ 1,2,3,4,5,4,3,21,3,5,23,4,2,313,32,2,3,4,1,22,3,4,5]
value = 4

while value in list_a:
    list_a.remove(value)
print(list_a)