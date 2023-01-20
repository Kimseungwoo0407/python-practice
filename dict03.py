# 딕셔너리 선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당 절임"
}

# 요소 제거 전 내용 출력
print("요소 제거 이전:", dictionary)

# 요소 제거
del dictionary["name"]
del dictionary["type"]

# 요소제거 이후
print("요소 제거 이후:", dictionary)