numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(numbers)//2):
    # j가 1,3,5,7이 나오려면 어떤 식을 사용할 지
    j = i*2+1
    print("i={},j={}".format(i,j))
    numbers[j] = numbers[j] **2

print(numbers)