
## 윈도우 프로그램의 기본 위젯: 라벨(Label)

# tkinter: GUI 관련 모듈을 제공해주는 표준 윈도우 라이브러리
# 윈도우 창을 출력할 때 반드시 입력
from tkinter import *

# Tk()는 기본이 되는 윈도우를 반환(루트 윈도우/베이스 윈도우)
window = Tk()
window.title("라벨 연습") # 윈도우 창에 제목 표시


# 라벨(label): 문자를 표현할 수 있는 위젯
# 부모 윈도우로 window 지정 --> 베이스 윈도우에 라벨이 출력
label1 = Label(window, text="오늘은 불금")

label2 = Label(window, text="열심히 놀자", font=("궁서체", 30), fg="blue", bg="#dddddd") # 폰트, 글자색, 배경색 설정 가능
# 색상 표현은 색상명, HEX 사용 가능

label3 = Label(window, text="화이팅", bg="magenta", width=20, height=5, anchor=SE) # 넓이, 높이, 위치 설정 가능
# anchor: 위젯이 어느 위치에 자리잡을 지 지정(N, NE, E, SE, S, SW, W, NW, CENTER)

# pack() 함수를 호출해야 화면에 출력
label1.pack()
label2.pack()
label3.pack()

# mainloop(): 윈도우 창에 키보드 누르기, 마우스 클릭 등 다양한 이벤트를 처리
window.mainloop()
