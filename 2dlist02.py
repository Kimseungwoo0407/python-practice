# 2차원 리스트에서 반복문 두번 사용

list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for items in list_of_list:
    for item in items:
        print(items)