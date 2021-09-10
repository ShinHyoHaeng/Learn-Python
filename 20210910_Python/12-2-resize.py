
## 윈도우 창 조절하기

# tkinter: GUI 관련 모듈을 제공해주는 표준 윈도우 라이브러리
# 윈도우 창을 출력할 때 반드시 입력
from tkinter import *

# Tk()는 기본이 되는 윈도우를 반환(루트 윈도우/베이스 윈도우)
window = Tk()

window.title("윈도우 창 연습") # 윈도우 창에 제목 표시
window.geometry("400x100") # 윈도우 창의 초기 크기를 400 * 100으로 지정
window.resizable(width=FALSE, height=FALSE) # 가로 세로의 크기가 변경되지 않도록 설정(변경하고 싶다면 TRUE || 1로 수정)

# mainloop(): 윈도우 창에 키보드 누르기, 마우스 클릭 등 다양한 이벤트를 처리
window.mainloop()
