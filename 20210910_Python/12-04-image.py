
## 윈도우 프로그램의 기본 위젯: 라벨(Label) - 이미지 출력

from tkinter import *

window = Tk()
window.title("이미지 연습") # 윈도우 창에 제목 표시

# PhotoImage: 이미지 출력
# step 1. 이미지 파일을 준비
photo1 = PhotoImage(file="0910_gif/dog.gif") # PhotoImage는 gif 파일만 지원
photo2 = PhotoImage(file="0910_gif/dog2.gif")

# step 2. Label() 옵션에서 image 속성을 지정해 글자대신 이미지 사용
label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)

# step 3. 화면에 출력(기본값은 상하정렬)
label1.pack(side=LEFT) # 왼쪽으로 정렬
label2.pack(side=RIGHT) # 오른쪽으로 정렬

window.mainloop()
