gen = input("염기 서열을 입력해주세요:")
counter ={
    "a": 0,
    "t": 0,
    "g": 0,
    "c": 0}

for i in gen:
    counter[i] += 1

for key in counter:
    print("{}의 개수: {}".format(key,counter[key]))