try:
    file = open("info.txt", "w")

    예외.발생하라()
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)