date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price)) # zip 함수를 사용해 data를 key로, close_price를 value로 가지는 딕셔너리를 생성. 
print(close_table)  # close_table을 출력.