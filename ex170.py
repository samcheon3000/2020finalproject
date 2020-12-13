total = 1   # 결과를 대입할 변수를 정한다. 변수 i를 차례로 곱해도 값에 영향을 끼치지 않도록 1이 되어야 한다.
for i in range(1,11):   # i의 값을 1부터 10까지로 정한다.
    total = total * i   # 처음 정한 total과 i를 곱한 뒤 그 값을 다시 total에 대입한다. 
print(total)            # 변수 i를 전부 곱한 total이 출력된다.