
## 객체지향: 메소드 오버라이딩

# 클래스 정의 부분
class Car :
    speed = 0
    def upSpeed(self, value):
        self.speed += value

        print("현재 속도(슈퍼 클래스) : %d" % self.speed)

# 서브 클래스
class Sedan(Car):
    # 속도 제한(150) --> Car의 upSpeed() 메소드를 재정의
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150 :
            self.speed = 150
        print("현재 속도(서브클래스) : %d" % self.speed)
    
# 서브 클래스
class Truck(Car):
   pass # 추가하거나 수정할 값 없음

# 변수 선언
sedan1, truck1 = None, None

# 메인 코드 부분
sedan1 = Sedan()
truck1 = Truck()

print("트럭 --> ", end="")
truck1.upSpeed(200)

print("승용차 --> ", end="")
sedan1.upSpeed(200)


## 출력 결과
'''
트럭 -->현재 속도(슈퍼 클래스) : 200
승용차 -->현재 속도(서브클래스) : 150
'''