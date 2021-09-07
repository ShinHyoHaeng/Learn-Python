## 2차원 리스트

# 빈 리스트 작성
list1=[]
list2=[]

# 리스트에 출력될 값 초기값 선언
value=1

# 2차원 리스트 생성
for i in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1=[] # list1을 초기화 하지 않으면 이전값(1,2,3,4)만 출력됨

# 2차원 리스트 출력
for i in range(0,3):
    for k in range(0,4):
        print("%3d" % list2[i][k], end="    ") # end="  " --> 가로로 출력되도록 
    print("")
