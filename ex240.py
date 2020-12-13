def 함수0(num) :    # num을 입력받아 num*2를 리턴하는 함수
    return num * 2

def 함수1(num) :    # num을 입력받아 함수0에 num + 2를 넣은 값을 리턴한다.
    return 함수0(num + 2)  # 즉, (num + 2) * 2를 리턴한다.

def 함수2(num) :   # num을 입력받아 함수1에 num + 10을 넣은 값을 리턴한다.
    num = num + 10  # 즉, ((num + 10) + 2) * 2를 리턴한다.
    return 함수1(num)

c = 함수2(2)     # 함수2에 2를 입력해 호출한다.
print(c)        # c를 출력한다. 
# 결과 
# 28 # :((2 + 10) + 2) * 2 이기 때문에