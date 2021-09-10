
## 객체지향: 클래스
# 클래스 정의 부분
class Car : # 클래스 생성
    
    # 필드 선언
    color = ""
    speed = 0

    # 메소드 선언
    def upSpeed(self, value): # self: 클래스 자신 --> 필드의 speed 변수 / 실제 넘겨 받는 매개변수는 value 한 개
        self.speed += value

    def downSpeed(self, value): # self: 클래스 자신 --> 필드의 speed 변수
        self.speed -= value

# 메인 코드 부분
myCar1 = Car() # 인스턴스 생성(인스턴스 = 클래스이름())

# 필드나 메소드 사용
myCar1.color = "빨강" # myCar1 인스턴스의 color 필드에 값 대입
myCar1.speed = 0 # myCar1 인스턴스의 speed 필드에 값 대입

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30) # myCar1 인스턴스의 메소드 호출
print("자동차1의 색상은 %s이며, 현재속도는 %d km입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 현재속도는 %d km입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print("자동차3의 색상은 %s이며, 현재속도는 %d km입니다." % (myCar3.color, myCar3.speed))
