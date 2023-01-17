# 정수를 특정 칸에 출력하기

output_a = "{:d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

# 기본
print(output_a)

# 특정 칸 출력
print(output_b)
print(output_c)

# 빈칸 0으로
print(output_d)
print(output_e)