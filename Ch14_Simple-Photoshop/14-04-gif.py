
## 프로그램 메뉴 생성: askopenfilename()
# 그림 파일인 GIF 파일을 선택한 다음 코드를 통해 사용 방법 확인

from tkinter import *
from tkinter.filedialog import * # tkinter.filedialog 모듈 import

# 함수 정의 부분
window = Tk()
window.geometry("400x100")

label = Label(window, text="선택된 파일 이름") # 라벨 준비
label.pack()

filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
# askopenfilename() 함수 사용
# 함수의 매개변수 중 parent는 부모 윈도우를 지정
# askopenfilename() 함수는 경로를 포함해 선택한 파일의 파일명을 반환

label.configure(text=str(filename)) # 선택한 filename 출력

window.mainloop()