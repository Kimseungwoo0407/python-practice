# 피타고라스의 정리

밑변 = float(input("밑변의 길이를 입력해주세요:"))
높이 = float(input("높이의 길이를 입력해주세요:"))

빗변 = (밑변**(2)+높이**(2))**(1/2)

print("= 빗변의 길이는 {}입니다.".format(빗변))