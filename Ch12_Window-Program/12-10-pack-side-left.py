
## 위젯의 배치와 크기 조절: 수평으로 정렬

from tkinter import *
window = Tk()

# Step 1. 버튼 인스턴스 3개 생성
button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

# Step 2. 버튼 3개를 화면에 수평으로 정렬해 출력
# side=LEFT: 버튼을 왼쪽부터 정렬
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

window.mainloop()