## 딕셔너리

'''
리스트는 대괄호[], 딕셔너리는 중괄호{}, 튜플은 소괄호()로 집합 생성

'''

# 학생 정보의 리스트 표현
student1=[1000,'홍길동','컴공']
print(student1[1])

# 리스트에 값 추가
student1.append('010-1234-5678')

# 리스트에 값 삭제
del(student1[0])

# 리스트 제일 뒤의 값을 빼내고 빼낸 값 삭제
student1.pop()
print(student1)

# 리스트의 모든 값 삭제
student1.clear()
print(student1)


# 학생 정보의 딕셔너리 표현
student={'학번':1000, '이름':'홍길동', '전공':'컴공'}
print(student['이름']) # 인덱스 대신 키 사용

# 딕셔너리에 값 추가
student['연락처'] = '010-1234-5678' # 키와 값 모두 입력 필요

# 딕셔너리에 값 삭제
del(student['학번'])

# 딕셔너리에서특정키의 값 삭제
student.pop('연락처')
print(student)

# 딕셔너리의 모든 값 삭제
student.clear()
print(student1)

