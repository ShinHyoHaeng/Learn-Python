## 함수

# 함수 정의 부분
def plus( v1, v2) :
    result = 0
    result = v1+v2
    return result

# 변수 선언 부분
hap = 0

# 메인 코드 부분
'''
hap = plus(100,200)
print("100과 200의 plus() 함수 결과는 %d" % hap)
'''
'''
# 값을 입력받아서 함수 결과 출력
a = int(input("더할 숫자를 입력하세요 : "))
b = int(input("더할 숫자를 입력하세요 : "))

hap = plus(a,b)
print("%d와 %d의 plus() 함수 결과는 %d" % (a,b,hap))
# % a,b,hap --> TypeError: not enough arguments for format string
'''


## 가변 매개변수(Arbitrary Argument List) 방식
# 함수 정의 부분
def para_func(*para) :
    result = 0
    for num in para : # 여기에 있는 'para'는 리스트 --> 매개변수가 para의 원소가 됨
        result = result + num

    return result

# 변수 선언 부분
hap = 0

# 메인 코드 부분
hap = para_func(10, 20)
print("매개변수 2개  함수 호출 결과 >> %d" % hap)

hap = para_func(10, 20, 30)
print("매개변수 3개  함수 호출 결과 >> %d" % hap)
