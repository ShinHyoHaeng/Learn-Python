
## 키보드/마우스 이벤트: 키보드 이벤트
# 위젯에서 키보드가 눌리면 발생하는 이벤트

from tkinter import *
from tkinter import messagebox

# 함수 정의 부분: 키보드가 눌릴 때 작동하는 함수 정의
def keyEvent(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : " + chr(event.keycode))
    #event.keycode: 눌린 키의 숫자값 --> chr() 함수를 이용해 문자로 변환

# 메인 코드 부분
window = Tk()

window.bind("<Key>", keyEvent)

window.mainloop()
