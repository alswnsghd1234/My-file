import itertools
import numpy as np

#itertools.produc(*L)
# -> 순회 가능한 여러 개의 객체를 순서대로 순회하는 이터레이터 생성
def GG():
    for a,b,c in itertools.product(range(4), range(3), range(3)):
        return a,b,c

# for문 3개 있는것과 같음

def LL():
    for a in range(4):
        for b in range(3):
            for c in range(3):
                return a,b,c

print(LL() == GG())

#itertools.combination(p, r)
# -> 이터레이터 객체 p에서 r의 가능한 모든 조합을 갖는 이터레이터를 생성
L = ['a', 'b', 'c', 'd']
for comb in itertools.combinations(L, 2):
    print(comb)
print( )
#itertlls.permutations(p,r)
# -> 이터레이터 객체 p에서 크기 r의 가능한 모든 순열을 갖는 이터레이터를 생성
for perm in itertools.permutations(L, 2):
    print(perm)

n1 = [1,2,3,4,5,6]

print(np[::2])