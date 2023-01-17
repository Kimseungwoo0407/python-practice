numbers = [273,103,5,32,65,9,72,800,99]

for number in numbers:
    if number / 100 >= 1:
        print(number,'는 3 자릿수입니다.')
    elif 1<=number / 10 < 10:
        print(number,'는 2 자릿수입니다.')
    else: print(number,'는 1자릿수입니다.')