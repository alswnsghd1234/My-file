import sys

a = [ n for n in range(10000)]
b = range(10000)

if len (a) == len(b):
    print(True)
print(type(b))
print(type(a))

# 실행시 걸리는 걸리는
print(sys.getsizeof(a))
print(sys.getsizeof(b))

