import pprint

a = [1,2,3,4,5,6,7]

for i,v in enumerate(a):
    print(i,v)

    print(divmod(i,v))
pprint.pprint(locals())