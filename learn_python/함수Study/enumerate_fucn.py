a = [1,2,3,4,5,6,7]
print(enumerate(a))

#list 형태로 index까지 반환
print(list(enumerate(a)))
#dictionary 형태로 index까지 반환
print(set(enumerate(a)))
#tuple 형태로 index까지 반환
print(tuple(enumerate(a)))

for _ in range(len(a)):
    print(_ , a[_])

print()
i = 0
for v in a:
    print(i,v)
    i += 1

print()

for i, v in enumerate(a):
    print(i,v)