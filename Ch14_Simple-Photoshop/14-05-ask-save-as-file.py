
## 프로그램 메뉴 생성: asksaveasfile()
# 코드 실행 시 [다른 이름으로 저장] 창 출력

from tkinter import *
from tkinter.filedialog import * # tkinter.filedialog 모듈 import

# 함수 정의 부분
window = Tk()
window.geometry("400x100")

label = Label(window, text="선택된 파일 이름") # 라벨 준비
label.pack()

saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*")))
# askopenfilename() 함수는 문자열(파일 경로, 파일명)만 반환 --> asksaveasfile() 함수는 다른 정보도 함께 반환
# mode = "w": 쓰기 모드
# defaultextension = ".jpg": 특별히 확장자를 지정하지 않으면 확장자를 jpg로 지정

label.configure(text=saveFp) # saveFp 자체를 text에 대입해 출력

window.mainloop()