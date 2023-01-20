# 딕셔너리 선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고","설탕","메타종아황산나트륨","치자황색소"],
    "origin":"필리핀"
}

# 존재 x 키 접근
value = dictionary.get("존재하지 않는 키")
print("값:", value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")