
## 윈도우 프로그램의 기본 위젯: 버튼

from tkinter import *

window = Tk()
window.title("버튼 연습") # 윈도우 창에 제목 표시

# 버튼 위젯 출력하기
# step 1. 버튼 생성하기
# command 옵션에 quit 명령 적용 --> 버튼을 클릭하면 IDLE 종료
button = Button(window, text="파이썬 종료", fg="red", command=quit) # 창을 닫는 명령 실행

# step 2. 버튼 출력
button.pack()

window.mainloop()
