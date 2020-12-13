리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:   # 변수 i에 리스트의 각 원소들을 대입한다.
    split = i.split(".")  # i를 "."을 기준으로 쪼개 배열에 저장한다. split[1]에 "."뒤의 문자, 즉 확장자가 저장되어 있다.
    if split[1] == "h" or split[1] == "c":   # split[1]이 논리 연산자 'or'에 의해 "h" 나 "c" 중 하나를 가지고 있으면 변수 i를 출력하는 조건문
        print(i)