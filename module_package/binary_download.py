from urllib import request

target = requeset.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드로 (바이너리일 경우 wb로 해야함)
file = open("output.png","wb")
file.write(output)
file.close()