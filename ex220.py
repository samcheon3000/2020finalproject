def print_max(a, b, c):
    answer = 0       # 답으로 사용할 변수 선언, 초기값은 어느 것과 비교해도 가장 작도록 0으로 한다.
    if a > answer:   # a가 answer 보다 클 경우
        answer = a   # a를 answer로 한다.
    if b > answer:   # b가 answer보다 클 경우 
        answer = b   # b를 answer로 한다. 그렇지 않을 경우 answer는 변하지 않는다.
    if c > answer:   # c가 answer보다 클 경우 
        answer = c   # c를 answer로 한다. 그렇지 않을 경우 answer는 변하지 않는다.
    print(answer)    # answer를 출력한다.

print_max(20, 31, 21)  # 인자를 넣어 함수 print_max를 호출한다. 차례대로 a, b, c가 된다.