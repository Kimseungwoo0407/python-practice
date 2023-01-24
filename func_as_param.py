def call_10_times(func):
    for i in range(10):
        func()

# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")
    
call_10_times(print_hello)