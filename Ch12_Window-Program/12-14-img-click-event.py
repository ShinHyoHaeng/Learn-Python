
## 키보드/마우스 이벤트: 지정된 위젯을 클릭했을 때 함수 호출

from tkinter import *
from tkinter import messagebox

# 함수 정의 부분
# 마우스 이벤트 발생 시 실행할 함수 정의
def clickImage(event) :
    messagebox.showinfo("마우스", "토끼 이미지에서 클릭 이벤트 실행")

# 메인 코드 부분
window = Tk()
window.geometry("400x400")

# 이미지 준비
photo = PhotoImage(file="gif/rabbit.gif")
label = Label(window, image=photo)

# 이미지를 넣은 라벨에 마우스 클릭 시 clickImage() 함수 실행
label.bind("<Button>", clickImage)

label.pack(expand=1, anchor=CENTER)
# expand = 미사용 공간 확보 --> 부모 위젯(윈도우) 크기만큼 위젯의 크기를 확장

window.mainloop()