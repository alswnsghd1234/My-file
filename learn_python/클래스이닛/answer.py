answer = []

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

lenlen = []

id_list = map(tuple, id_list )
for i in range(len(id_list)):
    lenlen += report.find(id_list[i])
print(lenlen)