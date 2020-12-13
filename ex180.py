low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []   # 비어있는 리스트 생성
for i in range(len(low_prices)):  # low_prices의 길이만큼 변수 i의 범위를 지정. 루프는 총 5번 반복한다.
    volatility.append(high_prices[i] - low_prices[i])  # 변동폭 리스트에 같은 위치의 high_prices 원소에서 low_prices 원소를 뺀 값을 추가한다.