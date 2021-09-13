## 튜플

'''
# 튜플
    한번 만들고 나면 변경할 수 없는 집합
    괄호()로 생성
    값을 수정할 수 없으며 읽기만 가능 --> 읽기 전용의 자료를 저장할 때 사용
# 리스트
    대괄호로 생성
'''

myTuple=(1,2,3)

# 튜플은 일반적으로 괄호( ) 없이도 사용 가능
myTuple=1,2,3 

print(myTuple) # 튜플 전체 출력 
print(myTuple[0]) # 특정 인덱스의 튜플 값 출력 --> 리스트와 동일하게 인덱스로 불러옴
#myTuple[1]=4 # 튜플 값은 수정 불가 --> 에러 출력 

# mytuple 새롭게 선언  --> 수정 X
myTuple=(1,) # 튜플의 요소가 하나밖에 없을 때에는 반드시 콤마(,) 삽입 필요
print(myTuple)
print(type(myTuple)) # tuple로 인식

# 콤마(,)를 쓰지 않으면
myTuple=(1)
print(myTuple)
print(type(myTuple)) # int로 인식
