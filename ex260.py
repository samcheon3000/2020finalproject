class OMG :         # "Oh my god"을 출력하는 함수 print()가 포함된 클래스 OMG
    def print() :
        print("Oh my god")

myStock = OMG()    # 클래스 OMG에 대한 인스턴스 생성
myStock.print()    # 실행하면 인자가 없어야 하지만 하나를 받았다는 오류가 발생한다. 파이썬 매서드의 첫 번째 인자로 항상 인스턴스가 전달되기 때문임.
# 해결하기 위해서는 함수를 def print(self)로 설정한다. 그러면 첫 번째 인자인 self에 대한 값은 파이썬이 자동으로 넘겨 아무것도 전달하지 않아 오류가 발생하지 않는다.
# 또는 인스턴스를 생성할 필요 없이 OMG.print()으로 함수를 호출할 수 있다.