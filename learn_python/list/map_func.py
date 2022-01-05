#map함수 표현식

def one_func(n):
    return n + 1

print(list(map(one_func, [2,34,5])))

#lambda 함수 표현식

print(list(map(lambda x: x+1,[2,34,5])))

#list comprehension 을 활용하자

a = [n +1 for n in range(10) if n % 2 ==1]
print(a)

#dictionary 형태도 comprehension 사용하자

a = {key:value for key, value in original.items()}

#위에 딕셔너리 풀어서 쓰면
a = {}
for key , value in original.items():
    a[key] = value
