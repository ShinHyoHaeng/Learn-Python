# 20210813. 신효행, 파이썬 기초 및 실습, 윈도우 프로그래밍 맛보기
# 윈도우 프로그래밍

# tkinter는 파이썬에서 GUI 관련 모듈을 제공해주는 표준 윈도우 라이브러리
from tkinter import *


## 변수 ##
window = None
canvas = None

# 선의 시작점과 끝점의 x,y 좌표값 저장
x1,y1,x2,y2 = None,None,None,None 


## 함수 ##
# 사용자 정의 함수, 함수의 정의부
def mouseClick(event):
    global x1,y1,x2,y2 # 전역변수 선언
    x1 = event.x # 첫번째 이벤트가 발생했을 때 x 좌표값을 x1에 저장
    y1 = event.y # 첫번째 이벤트가 발생했을 때 y 좌표값을 y1에 저장

def mouseDrop(event):
    global x1,y1,x2,y2 # 전역변수 선언
    x2 = event.x # 두번째 이벤트가 발생했을 때 x 좌표값을 x2에 저장
    y2 = event.y # 두번째 이벤트가 발생했을 때 y 좌표값을 y2에 저장

    # canvas.create_line(시작점x,시작점y,끝점x,끝점y)
    canvas.create_line(x1,y1,x2,y2,width=5,fill="red")


## 메인 코드 ##
    
# Tk(): 기본이 되는 윈도우를 반환. 루트 윈도우(Root Window)/베이스 윈도우(Base Window).
window = Tk()

# 윈도우 창에 제목 표시
window.title("그림판")

# window 안에 canvas 생성
canvas = Canvas(window, height=300, width=300)

# bind() 메서드: 원하는 이벤트와 원하는 함수 연결
canvas.bind("<Button-1>", mouseClick)
canvas.bind("<ButtonRelease-1>", mouseDrop)

# window 안에 canvas를 디스플레이
canvas.pack()

# 이 부분에서 화면을 구성하고 처리
window.mainloop()

