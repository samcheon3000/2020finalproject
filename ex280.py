import random     # 파이썬에 존재하는 random 패키지 호출. 

# 예금주, 잔액을 받아 계좌를 생성하는 함수가 포함된 클래스
class Account:   
    account_count = 0   # 계좌 생성 횟수 초기값
    def __init__(self, name, balance):
        self.deposit_count = 0    # 입금 횟수 초기값을 0으로 설정
        self.deposit_log = []     # 입금 내역을 담을 빈 리스트 생성
        self.withdraw_log = []    # 출금 내역을 담을 빈 리스트 생성

        self.name = name          # 전달받은 이름으로 예금주 설정
        self.balance = balance    # 전달받은 잔액으로 잔액 설정
        self.bank = "SC은행"      # 은행명 "SC은행" 설정

        # 3-2-6 의 계좌번호 생성
        num1 = random.randint(0, 999)     # 0~999 까지의 정수 중 하나를 랜덤하게 선정
        num2 = random.randint(0, 99)      # 0~99 까지의 정수 중 하나를 랜덤하게 선정
        num3 = random.randint(0, 999999)  # 0~999999 까지의 정수 중 하나를 랜덤하게 선정

        num1 = str(num1).zfill(3)  # 정수형 변수 num1을 문자열로 바꾸고 3자리가 되도록 설정. ex) 1 : 정수 -> '1' : 문자열 -> '001' : 3자리
        num2 = str(num2).zfill(2)  # 정수형 변수 num2을 문자열로 바꾸고 2자리가 되도록 설정. ex) 1 : 정수 -> '1' : 문자열 -> '01' : 2자리 
        num3 = str(num3).zfill(6)  # 정수형 변수 num3을 문자열로 바꾸고 6자리가 되도록 설정. ex) 1 : 정수 -> '1' : 문자열 -> '000001' : 6자리
        self.account_number = num1 + '-' + num2 + '-' + num3  # num1, num2, num3 사이에 '-'를 넣어 계좌번호 생성. ex) 001-01-000001
        Account.account_count += 1 # 계좌 생성 횟수 저장

    @classmethod    # 정적 매서드를 지원. 인스턴스를 만들지 않아도 class의 메서드를 바로 실행할 수 있다.
    def get_account_num(cls):   # cls: classmethod에서 '클래스'를 가리킨다. 이것으로 클래스의 어떤 속성에도 접근할 수 있다.
        print(cls.account_count)  # Account.account_count와 같은 의미. 

    def deposit(self, amount):   # 입금한 액수 amount를 받아 실행하는 함수
        if amount >= 1:          # 입금 액수가 1 이상일 경우 
            self.deposit_log.append(amount)  # 입금 내역에 액수를 추가
            self.balance += amount           # 잔액에 입금 액수를 더한다.

            self.deposit_count += 1          # 입금 횟수 저장
            if self.deposit_count % 5 == 0:  # 입금 횟수가 5의 배수일 때마다
                self.balance = (self.balance * 1.01) # 잔액의 0.01배인 이자 지급


    def withdraw(self, amount):     # 출금한 액수 amount를 받아 실행하는 함수
        if self.balance > amount:   # 잔액이 출금 액수보다 클 경우
            self.withdraw_log.append(amount)   # 출금 내역에 액수를 추가
            self.balance -= amount             # 잔액에서 액수를 뺀다.

    def display_info(self):    # 계좌에 대한 정보를 출력하는 함수, @classmethod 로 인해 class에 속한 함수의 매서드를 바로 실행할 수 있다.
        print("은행이름: ", self.bank)           # 설정한 은행 이름을 호출해서 출력.  
        print("예금주: ", self.name)              # 설정한 예금주명을 호출해서 출력.
        print("계좌번호: ", self.account_number)   # 생성한 계좌번호를 호출해서 출력.
        print("잔고: ", self.balance)             # 저장된 잔고를 호출해서 출력.

    def withdraw_history(self):      # 출금 내역을 출력하는 함수
        for amount in self.withdraw_log:  # 출금 내역 리스트의 길이만큼 돌아가는 루프. 출금내역 리스트의 원소를 저장하는 변수 amount
            print(amount)                 # 변수 amount를 출력한다.

    def deposit_history(self):      # 입금 내역을 출력하는 함수
        for amount in self.deposit_log:   # 입금 내역 리스트의 길이만큼 돌아가는 루프. 출금내역 리스트의 원소를 저장하는 변수 amount
            print(amount)                 # 변수 amount를 출력한다.


k = Account("Kim", 1000)   # 클래스 Account에 인자 "Kim"과 '1000'을 넣어 실행. 각각 예금주명과 잔액이다.
k.deposit(100)             # 100 입금
k.deposit(200)             # 200 입금
k.deposit(300)             # 300 입금

print("deposit")       # 구분을 위해 "deposit" 출력
k.deposit_history()    # 출금 내역을 출력하는 함수 deposit_history를 호출

k.withdraw(100)        # 100 출금
k.withdraw(200)        # 200 출금
print("withdraw")      # 구분을 위해 "withdraw" 출력
k.withdraw_history()   # 입금 내역을 출력하는 함수 withdraw_history를 호출