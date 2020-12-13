class Stock:     # 종목명, 종목코드, per, pbr, 배당수익률을 넣어 각각의 값을 리턴하는 함수 __init__를 포함하는 클래스 Stock
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name            # 종목명 리턴
        self.code = code            # 종목코드 리턴
        self.per = per              # per 리턴
        self.pbr = pbr              # pbr 리턴
        self.dividend = dividend    # 배당수익률 리턴

kind = []   # 빈 리스트 생성

# 클래스 Stock에 인자를 넣어 함수 __init__ 실행.
samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)  
handai = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

kind.append(samsung)   # 리스트 kind에 samsung을 추가
kind.append(handai)    # 리스트 kind에 handai를 추가
kind.append(LG)        # 리스트 kind에 LG를 추가

for i in kind:         # 변수 i가 리스트 kind에서 클래스 Stock의 객체를 바인딩한다.  
    print(i.code, i.per)   # samsung, handai, LG의 종목코드와 per을 출력.