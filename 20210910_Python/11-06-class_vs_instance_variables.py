
## 객체지향: 인스턴스 변수와 클래스 변수

# 클래스 정의 부분
class Car :
    color = "" # 필드: 인스턴스 변수
    speed = 0 # 필드: 인스턴스 변수
    count = 0 # 클래스 변수: 클래스 안에 공간이 할당된 변수

    # 생성자
    def __init__(self):
        self.speed = 0
        Car.count += 1

# 변수 선언
myCar1, myCar2 = None, None

# 메인 코드 부분
myCar1 = Car()
myCar1.speed = 30
print("자동차1의 현재 속도는 %dkm, 생산된 자동차 숫자는 총 %d대입니다." % (myCar1.speed, Car.count))
# 클래스 변수에 접근 시 '클래스이름.클래스변수명' || '인스턴스.클래스변수명' 방식으로 접근해야 클래스에 이미 생성되어 있는 공간 공유 가능

myCar2 = Car()
myCar2.speed = 60
print("자동차2의 현재 속도는 %dkm, 생산된 자동차 숫자는 총 %d대입니다." % (myCar2.speed, myCar2.count))


## 출력 결과
'''
자동차1의 현재 속도는 30km, 생산된 자동차 숫자는 총 1대입니다.
자동차2의 현재 속도는 60km, 생산된 자동차 숫자는 총 2대입니다.
'''