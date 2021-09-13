## 로또

import random

# 함수 정의 부분
def getNumber():
    return random.randrange(1,46) # 1 이상 46 미만의 임의의 정수값 생성

# 변수 선언 부분
lotto = [] # 빈 리스트 생성
num = 0

# 메인 코드 부분
print("** 로또 추첨 시작 ** \n")

while True:
    num = getNumber()

    if lotto.count(num) ==0: # 추출한 숫자가 이미 뽑힌 숫자와 동일한 숫자일 때
        lotto.append(num)

    if len(lotto)>=6: # 리스트의 개수가 6이 될 경우 탈출
       break

print("추첨된 로또 번호 ==> " , end='')
lotto.sort()
for i in range(0,6):
    print("%d " % lotto[i], end='')
