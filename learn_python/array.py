# arr = [i for i in range(10)]
# print(arr)
# print(arr[::2]) # 두 칸 간격으로
# print(arr[1::2]) #인덱스 1부터 두칸 간격으로
# print(arr[::-1]) #역순으로 -1씩
# print(arr[::-2]) #처음부터 끝까지 -2칸씩
# print(arr[3::-1]) #인덱스 3부터 끝까지 -1칸 간격으로
# print(arr[1:6:2]) #인덱스 1부터 인덱스 6까지 두 칸 간격으로

n = int(input())

num = 0
for i in range(1, n+1):
    num += i
print(num)
