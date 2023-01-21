number_list = [1,2,3,4,1,2,3,1,4,1,2,3]
counter = {}

for number in number_list:
    if number in counter:
        counter[number] = counter[number]+1
    else: counter[number]=1

print(number_list,"에서\n사용된 숫자의 종류는 {}개입니다.\n참고:".format(len(counter)),counter)
print(counter.keys)