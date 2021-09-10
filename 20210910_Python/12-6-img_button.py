
## 윈도우 프로그램의 기본 위젯: 버튼 - 이미지 버튼

from tkinter import *

# 버튼 클릭 시 에러(NameError: name 'messagebox' is not defined)
from tkinter import messagebox # 파이썬 3.6. 이후 버전에서 messagebox 오류 해결 방법

# 함수 정의 부분
def myFunc() :
    messagebox.showinfo("강아지 버튼", "강아지는 언제나 옳다")

# 메인 코드 부분
window = Tk()
window.title("이미지 버튼 연습") # 윈도우 창에 제목 표시

# 버튼 이미지 출력하기
# step 1. 버튼에 들어갈 이미지 생성하기
photo = PhotoImage(file="0910_gif/dog3.gif")

# step 2. 버튼 생성하기
button = Button(window, image=photo, command=myFunc) # myFunc()으로 넣으면 안됨

# step 3. 버튼 출력
button.pack()

window.mainloop()
