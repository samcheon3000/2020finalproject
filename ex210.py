def message1():  # "A"를 출력하는 함수
    print("A")

def message2():  # "B"를 출력하는 함수
    print("B")

def message3():
    for i in range (3) :  # 3번 돌아가는 루프
        message2()        # 함수 message2 호출
        print("C")        # "C" 출력
    message1()            # 루프에 속하지 않은 함수 message1 호출
# message2 와 print("C")가 총 세 번 반복된 후 message1 한 번 실행.
message3()   # 함수 message3 호출. 
#결과
# B
# C 
# B
# C
# B
# C
# A