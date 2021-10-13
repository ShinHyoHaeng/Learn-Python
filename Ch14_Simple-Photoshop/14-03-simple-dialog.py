
## 프로그램 메뉴 생성: 대화 상자
# 숫자나 문자를 입력받기 위해서 tkinter.simpledialog 모듈을 임포트 한 후 askinteger() 및 askstring()을 사용

from tkinter import *
from tkinter.simpledialog import * # tkinter.simpledialog 모듈 import

# 함수 정의 부분
window = Tk()
window.geometry("400x100")

label = Label(window, text="입력된 값") # 라벨 준비
label.pack()

value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6) 
# askinterger("제목","내용",옵션) 함수로 정수 입력 받음. minvalue는 최소값, maxvalue는 최대값

label.configure(text=str(value)) # 입력받은 숫자를 문자열로 변경해 라벨에 작성 
# 참고: 실수를 입력 받으려면 askfloat()을, 문자열을 입력받으려면 askstring()을 사용

window.mainloop()