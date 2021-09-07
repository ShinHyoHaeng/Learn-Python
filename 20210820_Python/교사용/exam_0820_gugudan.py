# 반복문을 이요한 구구단 출력

# 2단 출력
for y in range(1,10,1):
    print('2 x {} = {}'.format(y,2*y))

'''        
# 구구단 출력
for x in range(2,10,1):
    for y in range(1,10,1):
        print('{} x {} = {}'.format(x,y,x*y))
'''
'''
# 구구단 출력, 단마다 줄바꿈하기
for x in range(2,10,1):
    for y in range(1,10,1):
        print('{} x {} = {}'.format(x,y,x*y))
    print(' ')
'''
'''
# 구구단 출력, 단마다 가로로 출력하기
for x in range(2,10,1):
    for y in range(1,10,1):
        print('{} x {} = {}'.format(x,y,x*y), end="  ")
    print(' ')
'''
'''
#while문을 이용한 구구단
x=2 # 초기값
while x <10 : #조건식(끝값)
    y=1 # 초기값
    while y <10: #조건식(끝값)
        print('{} x {} = {}'.format(x,y,x*y), end="  ")
        y=y+1 #증감식
    print(' ')
    x=x+1 #증감식
'''








        
    
    
