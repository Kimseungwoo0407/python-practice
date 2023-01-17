import datetime

now = datetime.datetime.now()

answer = input("입력:")

if "안녕" in answer:
    print("안녕하세요")
elif "몇시" in answer:
    print("지금은 {}시입니다.".format(now.hour))
else : print(answer)