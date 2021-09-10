
## 윈도우 창의 기본 구성

# tkinter: GUI 관련 모듈을 제공해주는 표준 윈도우 라이브러리
# 윈도우 창을 출력할 때 반드시 입력
from tkinter import *

# Tk()는 기본이 되는 윈도우를 반환(루트 윈도우/베이스 윈도우)
window = Tk()

'''
화면을 구성하고 처리
'''

# mainloop(): 윈도우 창에 키보드 누르기, 마우스 클릭 등 다양한 이벤트를 처리
window.mainloop()
