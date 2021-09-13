## 계산기 함수

# 함수 정의 부분
def calc(a,b,op) :
    result = 0
    if op == '+' :
        result = a+b
    elif op == '-' :
        result = a-b
    elif op == '*' :
        result = a*b
    elif op == "/" :
        result = a/b

    return result


# 변수 선언 부분
res = 0
var1, var2, oper = 0, 0, ""

## 메인 코드 부분
oper = input("계산 입력 (+,-,*,/) : ")
var1 = input("첫번째 숫자 입력 : ")
var2 = input("두번째 숫자 입력 : ")

res = calc(var1,var2,oper)

print("## 계산 결과 : %d %s %d = %d" % (var1,oper,var2,res))

