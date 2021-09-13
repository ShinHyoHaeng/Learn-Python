
## 키보드/마우스 이벤트(응용)
# 클릭된 버튼에 따라 출력되는 텍스트 변경

from tkinter import *
from tkinter import messagebox

# 함수 정의 부분
# 마우스 이벤트 시에 작동할 clickLeft() 함수 정의
def clickLeft(event) :
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")

def clickCenter(event) :
    messagebox.showinfo("마우스", "마우스 중간 버튼이 클릭됨")

def clickRight(event):
    messagebox.showinfo("마우스", "마우스 오른쪽 버튼이 클릭됨")

window = Tk()

# window.bind() 함수에 각각 마우스 이벤트 설정
# 윈도우 창을 의미하는 window 변수 사용 --> 윈도우의 아무데나 클릭해도 bind() 함수 작동
window.bind("<Button-1>", clickLeft) # 마우스 왼쪽 버튼 클릭 --> clickLeft() 함수
window.bind("<Button-2>", clickCenter) # 마우스 중간 버튼 클릭 --> clickCenter() 함수
window.bind("<Button-3>", clickRight) # 마우스 오른쪽 버튼 클릭 --> clickRight() 함수

window.mainloop()