
## 프로그램 메뉴 생성 : 함수
# 메뉴를 선택하면 작동하도록 코드 추가

from tkinter import *
from tkinter import messagebox  # 파이썬 3.6. 이후 버전에서 messagebox 오류 해결 방법

# 함수 정의 부분
def func_open():
    messagebox.showinfo("메뉴 선택", "열기 메뉴를 선택함")

def func_exit():
    window.quit()
    window.destroy()

# 메인 코드 부분
window = Tk()

mainMenu = Menu(window)  # Menu(부모 윈도우)로 mainMenu 변수 생성 --> mainMenu는 메뉴 자체를 나타내는 변수
window.config(menu=mainMenu)  # 생성한 메뉴 자체를 윈도우 창의 메뉴로 지정

fileMenu = Menu(mainMenu)

# 상위 메뉴인 [파일] 메뉴를 생성하고 메뉴 자체에 부착
mainMenu.add_cascade(label="파일", menu=fileMenu)  # [파일] 메뉴는 확장 필요 --> add_cascade() 함수 사용

# [파일] 메뉴 하위에 [열기] 메뉴 준비
# [열기] 메뉴는 선택 할 때 동작 필요 --> add_command() 함수 사용
# 선택 시에 실행될 함수이름을 command 값으로 사용
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()  # 메뉴 사이의 구분 줄 삽입
fileMenu.add_command(label="종료", command=func_exit)

window.mainloop()
