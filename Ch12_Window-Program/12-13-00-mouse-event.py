
## 키보드/마우스 이벤트

from tkinter import *
from tkinter import messagebox

# 함수 정의 부분
# 마우스 이벤트 시에 작동할 clickLeft() 함수 정의
def clickLeft(event) :
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")

window = Tk()

# window.bind() 함수에 마우스 왼쪽 클릭 시에 나오는 이벤트인 <Button-1>와 clickLeft() 함수 설정
# 윈도우 창을 의미하는 window 변수 사용 --> 윈도우의 아무데나 클릭해도 bind() 함수 작동
window.bind("<Button-1>", clickLeft)

window.mainloop()