import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] 

변동폭 = float(btc['max_price']) - float(btc['min_price'])  # 딕셔너리 btc에서 키 'max_price'와 'min_price'를 실수형 변수로 불러와 최고가 - 최저가를 변동폭으로 저장한다.  
시가 = float(btc['opening_price'])  # 딕셔너리 btc에서 키 'opening_price'를 불러와 실수형 변수로 저장한다. 시가(시작 거래금액)이 된다.
최고가 = float(btc['max_price'])     # 딕셔너리 btc에서 키 'max_price'를 불러와 실수형 변수로 저장한다. 최고가(최고 거래금액)이 된다.

if (변동폭 + 시가) > 최고가:  # 시가와 변동폭의 합이 최고가보다 클 경우 '상승장'을, 작을 경우 '하락장'을 출력한다.
    print("상승장")
else:
    print("하락장")
