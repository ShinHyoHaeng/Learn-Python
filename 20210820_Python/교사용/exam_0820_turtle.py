#import turtle
#import turtle as t

'''
# 정사각형 그리기
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
'''

'''
#정삼각형 그리기
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
'''
'''
#정오각형 그리기
t.shape("turtle") #거북이 모양 바꾸기
t.speed(10) # 거북이 속도 조절하기
t.color("purple","blue") # 선색, 면색 지정
t.begin_fill() # 채우기 시작
'''
'''
t.forward(100) # 앞으로 나아가기
t.right(60) # 오른쪽 방향을 각도만큼 회전하기
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
'''
'''
for i in range(0,6,1):
    t.forward(100)
    t.right(60)
'''
'''
for i in [0,1,2,3,4,5]:
    t.forward(100)
    t.right(60)
'''
'''
for (i=0; i<6;1++) {
t.forward(100)
t.right(60)
}
'''
'''
t.end_fill()  # 채우기 종료
#t.clear() # 거북이 지우기
'''


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    print(pos(), abs(pos()))
    
    if abs(pos()) < 1:
        break
end_fill()
done()




