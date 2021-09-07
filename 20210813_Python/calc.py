# 20210813. 신효행, 파이썬 기초 및 실습, 계산기 프로그래밍
# 계산기 프로그래밍

# 사용자로부터 값을 입력받아 변수 값으로 대입
# int() 함수를 이용해 정수로 변환

a=int(input("연산할 첫번째 숫자를 입력하세요:"))
b=int(input("연산할 두번째 숫자를 입력하세요:"))

# 산술연산자로 처리한 다음 result 변수 값으로 대입
result=a+b

# 연산 결과 출력
print(a,"+",b,"=",result)


result=a-b
print(a,"-",b,"=",result)
result=a*b
print(a,"*",b,"=",result)
result=a/b
print(a,"/",b,"=",result)
