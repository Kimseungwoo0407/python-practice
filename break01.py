# continue 키워드
numbers = [5,15,6,20,7,25]

# 반복 돌립니다.
for number in numbers:
    # number가 10보다 작으면 다음 반복
    if number < 10:
        continue
    # 출력
    print(number)