
## 윈도우 프로그램의 기본 위젯: 라디오버튼

from tkinter import *

window = Tk()
window.title("라디오버튼 연습") # 윈도우 창에 제목 표시


# 함수 정의 부분
# var 변수의 값에 따라 윈도우 하단 라벨 label의 텍스트 변경
# 위젯명.configure(옵션=값): 해당 위젯의 옵션 값을 변경해주는 함수
def myFunc() :
    if var.get() == 1 :
        label.configure(text = "파이썬")
    elif var.get() == 2 :
        label.configure(text = "C++")
    else :
        label.configure(text = "Java")


# 메인 코드 부분
# IntVar() : 정수형 형식의 변수를 생성하는 함수
var = IntVar()

# 3개의 라디오버튼 준비
# 옵션 중 variable 값이 동일해야 하나의 그룹으로 인정

# rb1 버튼을 선택하면 var 값으로 1이 대입
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc)

# rb2 버튼을 선택하면 var 값으로 2가 대입
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = myFunc)

# rb3버튼을 선택하면 var 값으로 3이 대입
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = myFunc)

# Label로 텍스트 위젯 label 생성
label = Label(window, text = "선택한 언어", fg = "red")

# 3개의 라디오버튼과 1개의 텍스트 출력
rb1.pack()
rb2.pack()
rb3.pack()
label.pack()


window.mainloop()
