
## 키보드/마우스 이벤트: 이벤트 매개변수
# 마우스를 클릭할 때마다, 어떤 마우스가 클릭되었는지 보여주고 클릭한 좌표도 출력하는 프로그램

from tkinter import *

# 함수 정의 부분
# 마우스 이벤트 발생 시 실행할 함수 정의
def clickMouse(event) :
    txt = ""
    if event.num == 1 :
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3 :
        txt += "마우스 오른쪽 버튼이 ("

    txt += str(event.x)+", "+ str(event.y)+")에서 클릭됨"
    label.configure(text=txt)

# 메인 코드 부분
window = Tk()
window.geometry("400x400")

# 마우스 이벤트가 발생되면 label의 text가 clickMouse() 함수의 txt로 변경
label = Label(window, text = "이 곳이 바뀜")

# 윈도우 창에 마우스 클릭 --> clickMouse() 함수 실행
window.bind("<Button>", clickMouse)

label.pack(expand=1, anchor=CENTER)

window.mainloop()