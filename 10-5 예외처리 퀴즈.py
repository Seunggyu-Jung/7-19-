# 항상 대기 손님이 있는 치킨집이 있다
# 대기 손님의 치킨요리 시간을 줄이고자 자동 주문 시스템을 제작했다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시요.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어오면 valueerr 로 처리 
          # 출력 메시지 : "잘못된 입력값을 입력 하셨습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
            # 치킨 소진시 사용자 정의 에러[SoldOutErr] 를 발생시키고 종료
            # 출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

#코드

class SoldOutErr(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):  # 이게 멀까??
        return self.msg


chicken = 10
waiting = 1
try:
    while(True):
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order < 1:
            raise ValueError
        if order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
        waiting += 1
        chicken -= order
        if chicken < 0:
            raise SoldOutErr("재고가 소진되어 더 이상 주문을 받지 않습니다.")
except ValueError:
    print("잘못된 값을 입력하셨습니다.")
except SoldOutErr as err:
    print(err)
