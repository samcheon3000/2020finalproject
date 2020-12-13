per = ["10.31", "", "8.00"]

for i in per: 
    try:           # 리스트 per에 대해 수행. 문자열을 실수형 변수로 바꿔 출력한다.
        print(float(i))  
    except:        # 예외 발생. per의 두번째 원소는 실수형으로 바꿀 수 없다.
        print(0)   # 그 경우 0 을 출력.
    else:          # 예외가 발생하지 않을 경우 try와 같이 출력한다.
        print("예외가 발생하지 않음") 
    finally:       # 항상 출력한다.
        print("예외 발생 여부 상관없이 항상 수행") 
        