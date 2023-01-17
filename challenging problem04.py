number = int(input("정수를 입력해주세요:"))


if number % 2 == 0:
    print(number,"은 2로 나누어 떨어지는 숫자입니다.")
else:
    print(number,"은 2로 나누어 떨어지지 않는 숫자입니다.")

if number % 3 == 0:
    print("{}은 3으로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print(number,"은 3으로 나누어 떨어지지 않는 숫자입니다.")

if number % 4 == 0:
    print("{}은 4로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print(number,"은 4로 나누어 떨어지지 않는 숫자입니다.")

if number % 5 == 0:
    print("{}은 5로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print(number,"은 5로 나누어 떨어지지 않는 숫자입니다.")


    