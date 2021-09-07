## 리스트
# 4개의 값을 입력받아 더하는 프로그램 작성

# 리스트 사용 전
'''
# 파이썬에서는 변수를 선언하고 초기화를 해주지 않아도 됨
a,b,c,d = 0,0,0,0 
hap = 0

a = int(input("1번째 숫자:"))
b = int(input("2번째 숫자:"))
c = int(input("3번째 숫자:"))
d = int(input("4번째 숫자:"))

hap = a+b+c+d

# %d: 정수형 자료
print("합계 : %d" % hap)
'''


# 리스트 사용
'''
# 리스트에서는 초기화 필요 --> 개수를 알려주기 위해서
aa=[0,0,0,0]
hap = 0

aa[0] = int(input("1번째 숫자:"))
aa[1] = int(input("2번째 숫자:"))
aa[2] = int(input("3번째 숫자:"))
aa[3] = int(input("4번째 숫자:"))

hap = aa[0]+aa[1]+aa[2]+aa[3]

print("합계 : %d" % hap)
'''


# 리스트와 반복문 for의 활용
'''
aa=[0,0,0,0]
hap = 0

for i in range(0,4,1): # for i in range(초기값, 끝값+1, 증가값)
    aa[i] = int(input(str(i+1)+"번째 숫자: ")) # 숫자와 문자열은 + 연산 불가 --> str() 활용
    hap += aa[i]

print("합계 : %d" % hap)
'''



# append() 함수 사용
# 융통성 있게 확장할 수 있도록 빈 리스트 생성
'''
aa = []

print(aa)
aa.append(0)
print(aa)
aa.append(0)
print(aa)
'''

# for문으로 수정
'''
aa = []
hap = 0

for i in range(0,4): # for i in range(값1,값2) --> 증감식 생략
        aa.append(0)
print(aa)
'''


# append와 for문을 사용해 리스트 생성
'''
aa=[]
hap = 0

for i in range(0,4,1):
    aa.append(0)
    aa[i] = int(input(str(i+1)+"번째 숫자: "))
    hap += aa[i]

print("합계 : %d" % hap)
'''


aa=[]
hap = 0

for i in range(0,4,1):
    aa.append(0)
    aa[i] = int(input(str(i+1)+"번째 숫자: "))
    print(aa[i])
    hap += aa[i]

print("합계 : %d" % hap)
print(aa)

# 리스트이름[시작:끝+1]
print(aa[1:3]) # aa의 1부터 2개의 값(aa[1],aa[2]) 출력

