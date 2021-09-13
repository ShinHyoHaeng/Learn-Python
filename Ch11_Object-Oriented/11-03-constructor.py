
## 객체지향: 생성자

# 클래스 정의 부분
class Car : # 클래스 생성
    
    # 필드 선언
    color = ""
    speed = 0

    # 생성자: 인스턴스를 생성하면 무조건 호출
    def __init__(self):
        self.color = "빨강"
        self.speed = 0

    # 메소드 선언
    def upSpeed(self, value): # self: 클래스 자신 --> 필드의 speed 변수 / 실제 넘겨 받는 매개변수는 value 한 개
        self.speed += value

    def downSpeed(self, value): # self: 클래스 자신 --> 필드의 speed 변수
        self.speed -= value


# 메인 코드 부분
# 생성자 호출 --> 인스턴스에 필드 값 대입 필요 X
myCar1 = Car()
myCar2 = Car()

print("자동차1의 색상은 %s이며, 현재속도는 %d km입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재속도는 %d km입니다." % (myCar2.color, myCar2.speed))

