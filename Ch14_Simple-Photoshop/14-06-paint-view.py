
## 명화 감상 프로그램

from tkinter import *
from tkinter.filedialog import * # tkinter.filedialog 모듈 import

# 함수 정의 부분
# [파일 열기]를 하면 실행되는 함수
def func_open():
    filename = askopenfilename(parent=window, filetype=(("GIF 파일","*.gif"), ("모든 파일", "*.*"))) # askopenfilename()으로 파일 선택
    photo = PhotoImage(file = filename) # PhotoImage() 함수 처리
    pLabel.configure(image = photo) # 라벨에 이미지 표시
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

# 메인 코드 부분
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

# 윈도우 창에 선택한 gif 그림을 출력하기 위해 라벨 준비
# 처음 실행되면 선택된 그림 X --> PhotoImage()에 별도의 매개변수 없이 빈 그림만 준비
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label="파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command = func_exit)

window.mainloop()