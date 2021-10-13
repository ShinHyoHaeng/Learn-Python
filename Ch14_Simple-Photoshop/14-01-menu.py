
## 프로그램 메뉴 생성

from tkinter import *

window = Tk()

mainMenu = Menu(window) # Menu(부모 윈도우)로 mainMenu 변수 생성 --> mainMenu는 메뉴 자체를 나타내는 변수
window.config(menu=mainMenu) # 생성한 메뉴 자체를 윈도우 창의 메뉴로 지정

fileMenu = Menu(mainMenu)

# 상위 메뉴인 [파일] 메뉴를 생성하고 메뉴 자체에 부착
mainMenu.add_cascade(label="파일", menu = fileMenu) # [파일] 메뉴는 확장 필요 --> add_cascade() 함수 사용

# [파일] 메뉴 하위에 [열기] 메뉴 준비
fileMenu.add_command(label="열기") # [열기] 메뉴는 선택 할 때 동작 필요 --> add_command() 함수 사용
fileMenu.add_separator() # 메뉴 사이의 구분 줄 삽입
fileMenu.add_command(label="종료")

window.mainloop()

