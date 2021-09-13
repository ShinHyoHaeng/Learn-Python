
## 객체지향: 클래스 상속

# 클래스 정의 부분
# 승용차(Sedan)과 트럭(Truck)의 공통된 특징을 자동차(Car)라는 클래스로 생성
class Car :
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

# class 서브 클래스(슈퍼 클래스)
class Sedan(Car): # Car를 상속받은 후 필요한 필드와 메소드 추가
    seatNum = 0 # 좌석 수

    def getSeatNum(self): # 좌석 수 알아보기
        return self.seatNum

# class 서브 클래스(슈퍼 클래스)
class Truck(Car): # Car를 상속받은 후 필요한 필드와 메소드 추가
    capacity = 0 # 적재량

    def getCapacity(self): # 적재량 알아보기
        return self.capacity


# 변수 선언
sedan1, truck1 = None, None

# 메인 코드 부분
sedan1 = Sedan()
truck1 = Truck()

# Car(슈퍼 클래스)의 메소드 사용 가능
sedan1.upSpeed(100)
truck1.upSpeed(80)

sedan1.seatNum = 5
truck1.capacity = 50

print("승용차의 속도는 %d km, 좌석 수는 %d개입니다." % (sedan1.speed, sedan1.getSeatNum()))
print("트럭의 속도는 %d km, 총 중량은 %d톤입니다." % (truck1.speed, truck1.getCapacity()))


## 출력 결과
'''
승용차의 속도는 100 km, 좌석 수는 5개입니다.
트럭의 속도는 80 km, 총 중량은 50톤입니다.
'''