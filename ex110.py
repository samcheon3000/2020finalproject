if True :          # 입력받은 값이 참이면 아래의 조건문을 수행한다.
    if False:      # 거짓이라면 첫번째 if 문에서 else로 넘어가기에 실행될 일이 없는 조건이다.
        print("1") 
        print("2")
    else:          # 처음에 입력받은 값이 참이므로 "3"이 출력된다.
        print("3")
else :             # 처음에 입력받은 값이 거짓일 때에는 "4"가 출력된다.
    print("4")
print("5")         # 조건문에 속하지 않은 문장이기에 어떤 조건이든 출력된다.
# 결과
# 3
# 5 