import math
#정수


output_a = "{:d}".format(52)

#특정 칸에 출력하기

output_b = "{:5d}".format(52)
output_c = "{:5d}".format(52)

#빈칸을 0으로 채우기

output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)