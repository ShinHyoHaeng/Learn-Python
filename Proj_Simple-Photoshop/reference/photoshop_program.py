from tkinter import * # 윈도우 프로그램
from tkinter import messagebox # 메세지 박스를 사용하기 위해서
from tkinter.filedialog import * # 파일 입출력을 위한 다이얼로그창
from tkinter.simpledialog import * # 문자와 숫자를 입력하기 위한 다이얼로그창
from wand.image import * # 이미지 처리를 도와주는 외부 라이브러리 / jpg이미지 처리가능 하게해줌
import tkinter as tk
import tkinter.font as tkFont

## 함수 정의 ##
def displayImage(img, width, height) :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY

    #w.geometry(str(width) + "x" + str(height)) # 창을 이미지 크기에 맞기 변경
    
    if canvas != None : # 기존의 캔버스가 존재한다면 캔버스 삭제후 새로 만들어서 사용하기 위해 
        canvas.destroy()

    canvas = Canvas(w, width=width, height=height) # 캔버스 생성
    paper = PhotoImage(width=width, height=height)
    canvas.create_image( (width/2, height/2), image=paper, state="normal")

    blob = img.make_blob(format='RGB') # 이미지를 바이너리 코드로 변환 해주는 함수, 배열의 형태로 저장
    for i in range(0, width) :
        for j in range(0, height) :
            r = blob[(i*3*width) + (j*3) + 0] # blob[0..3..6..9] 값을 r에 저장
            g = blob[(i*3*width) + (j*3) + 1] # blob[1..4..7..10] 값을 g에 저장
            b = blob[(i*3*width) + (j*3) + 2] # blob[2..5..8..11] 값을 b에 저장
            # paper에 칼라로 점을 찍어줌, 세로로 높이만큼 찍고 가로를 너비만큼 반복
            paper.put("#%02x%02x%02x"% (r,g,b), (j,i)) # r,g,b값을 (02x)에 의해 각각 두자리 16진수로 변환하여 rgb값으로 결합한 후 (j,i)에 찍어줌
            # print(r,g,b) # r, g, b값 체크
            #print("#%02x%02x%02x, (%d, %d)" % (r,g,b, k,i)) # r,g,b값 을 16진수로 변환 결과 출력 테스트 
    canvas.place(x=(1045-width)/2, y=(920-height)/2)

def func_open() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    # askopenfilename() 함수는 파일 열기 대화상자를 나타내어 그림 파일 선택 
    readFp = askopenfilename(parent=w, filetypes=(("모든 그림파일", "*.jpg;*.jpeg;*.png;*.tif;*.gif"), ("모든 파일", "*.*")))
    photo = Image(filename=readFp) # jpg를 사용하기 위해 Photoimage() 가 아닌 wand의 Image() 사용
    oriX = photo.width
    oriY = photo.height

    photo2 = photo.clone() # 원본 이미지 복사
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY) # 복사된 photo2를 캔버스의 페이퍼에 디스플레이하기 위한 사용자 정의 함수

    # 파일 이름 출력
    font = tkFont.Font(family="맑은 고딕", size=8)
    tLabel = Label(w, text=readFp, background="#e1e1e1", fg="#222222", font=font)
    tLabel.place(x=44, y=39)

    # 파일 뒤 그림 추가 (테스트중)
    #aaX = len(readFp) * 7 - 4
    #tbgImage = PhotoImage(file="./images/text.png")    
    #canvas.create_image(320, 39, image=tbgImage, state="normal")
    
    # 비활성화 메뉴 활성화
    fileMenu.entryconfigure("저장", state=NORMAL)
    fileMenu.entryconfigure("되돌리기", state=NORMAL)
    imageMenu1.entryconfigure("확대", state=NORMAL)
    imageMenu1.entryconfigure("축소", state=NORMAL)
    imageMenu1.entryconfigure("상하 반전", state=NORMAL)
    imageMenu1.entryconfigure("좌우 반전", state=NORMAL)
    imageMenu1.entryconfigure("회전", state=NORMAL)
    imageMenu1.entryconfigure("색상 조정", state=NORMAL)
    imageMenu2.entryconfigure("밝게", state=NORMAL)
    imageMenu2.entryconfigure("어둡게", state=NORMAL)
    imageMenu2.entryconfigure("선명하게", state=NORMAL)
    imageMenu2.entryconfigure("탁하게", state=NORMAL)
    imageMenu2.entryconfigure("색조 조절", state=NORMAL)
    imageMenu2.entryconfigure("흑백이미지", state=NORMAL)
    imageMenu3.entryconfigure("흐리게", state=NORMAL)
    imageMenu3.entryconfigure("더 흐리게", state=NORMAL)
    imageMenu3.entryconfigure("가우시안", state=NORMAL)
    imageMenu3.entryconfigure("동작", state=NORMAL)
    imageMenu3.entryconfigure("방사형 흐림효과", state=NORMAL)
    imageMenu3.entryconfigure("확산", state=NORMAL)
    imageMenu3.entryconfigure("흑백 가장자리", state=NORMAL)
    imageMenu3.entryconfigure("엠보스", state=NORMAL)
    imageMenu3.entryconfigure("석고", state=NORMAL)
    imageMenu3.entryconfigure("스케치", state=NORMAL)
    imageMenu3.entryconfigure("굴절", state=NORMAL)
    
    
    
def func_save() :
    global w, canvas, paper, photo, photo2, oriX, oriY

    # window에 있는 파일을 저장 / mode=쓰기모드 저장 / 기본저장 파일형식 .jpg 파일 / 파일 저장 형태 선택 
    saveFp = asksaveasfile(parent = w, mode = "w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*")))
    savePhoto = photo2.convert("jpg") # 결과 이미지인 photo2를 jpg로 변환
    savePhoto.save(filename=saveFp.name) # 파일 저장 대화창에서 입력받은 파일 이름으로 저장

def func_revert() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    photo2 = photo.clone()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
    
def func_exit() :
    w.quit()
    w.destroy()

def func_zoomin() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    tmpX, tmpY = 0, 0
    scale = askinteger("확대배수", "확대할 배수를 입력하세요(2~4)", minvalue=2, maxvalue=4)
    tmpX = int(newX*scale)
    tmpY = int(newY*scale)
    if tmpX >= 750 :
        tmpX = 750
    if tmpY >= 750 :
        tmpY = 750
    
    photo2.resize(newX*scale, newY*scale) # Wand 라이브러리에서 제공하는 resize(가로,세로)함수를 사용
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_zoomout() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    scale = askinteger("축소배수", "축소할 배수를 입력하세요(2~4)", minvalue=2, maxvalue=4)
    photo2.resize(int(newX/scale), int(newY/scale))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_mirror1() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    photo2.flip() # 상하 반전 시키는 함수
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_mirror2() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    photo2.flop() # 좌우 반전 시키는 함수
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_rotate() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    photo2 = photo.clone()
    photo2.rotate(degree) # 회전 시키는 함수
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_bright() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    value = askinteger("밝게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)
    photo2.modulate(value, 100, 100) # 이미지 조절 하는 함수 / modulate(명도값, 채도값, 색상값) / 기본 명도값 100을 기준으로 낮으면 어둡 높으면 밝
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_dark() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    value = askinteger("어둡게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_clear() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    value = askinteger("선명하게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_unclear() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY

    value = askinteger("탁하게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_hue() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY

    value = askinteger("색조 조절", "값을 입력하세요(0~200)", minvalue=0, maxvalue=200)
    photo2.modulate(100, 100, value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_bw() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    photo2.type="grayscale"
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_blur() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    value = askinteger("흐림 정도", "값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    photo2.blur(radius=0, sigma=value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_adblur() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    value = askinteger("흐림 정도", "값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    photo2.blur(radius=value*2, sigma=value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_gausblur() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    value = askinteger("흐림 정도", "값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    photo2.gausiian_blur(sigma=value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_motoinblur() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    value1 = askinteger("흐림 정도", "값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    value2 = askinteger("방향", "값을 입력하세요(0~360)", minvalue=0, maxvalue=360)
    photo2.motion_blur(radius=value1*2, sigma=value1, angle=value2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_rotationblur() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    value = askinteger("방향", "값을 입력하세요(0~360)", minvalue=0, maxvalue=360)
    photo2.rotational_blur(angle=value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_Spread() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    value = askinteger("확산 정도", "값을 입력하세요(0~20)", minvalue=0, maxvalue=20)
    photo2.spread(radius=value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_edge() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    photo2.transform_colorspace('gray')
    photo2.edge(radius=1)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_emboss() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY

    photo2.transform_colorspace('gray')
    photo2.emboss(radius=3.0, sigma=1.3)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_shade() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY

    value = askinteger("돌출 정도", "값을 입력하세요(0~400)", minvalue=0, maxvalue=400)
    photo2.shade(gray=True, azimuth=value, elevation=45.0)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_sketch() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY

    photo2.transform_colorspace("gray")
    photo2.sketch(0.5, 0.0, 98.0)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_swirl() :
    global w, canvas, paper, photo, photo2, oriX, oriY, newX, newY

    value = askinteger("굴절 정도", "값을 입력하세요(-360~360)", minvalue=-360, maxvalue=360)
    photo2.swirl(degree=value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
    
## 변수 선언 ##
# 모든 함수들이 공통적으로 사용할 전역 변수들
w, canvas, paper = None, None, None 
photo, photo2 = None, None # photo는 처음 불러들인 원본 이미지, photo2는 처리 결과를 저장할 복사본
oriX, oriY = 0, 0 # 원본 이미지의 폭과 높이를 저장하는 변수

## 메인 코드 ##
w = tk.Tk()
w.geometry("1278x885")
w.title("미니 포토샵")

# 메뉴 생성
mainMenu = Menu(w) # 메뉴바 생성
w.config(menu=mainMenu) # 부모 윈도우에 메뉴 출력

fileMenu = Menu(mainMenu, tearoff=0) # 상위 메뉴 생성
mainMenu.add_cascade(label="파일", menu=fileMenu) # 메뉴바에 상위 메뉴 추가 / add_cascade를 사용해야 상위메뉴가 연결되어 나온다.
fileMenu.add_command(label="열기", command=func_open) # 상위 메뉴에 하위 메뉴 추가 / 이벤트를 연결 하기 위해 command 사용
fileMenu.add_separator()
fileMenu.add_command(label="저장", command=func_save, state=tk.DISABLED)
fileMenu.add_command(label="되돌리기", command=func_revert, state=tk.DISABLED)
fileMenu.add_separator() # 구분줄 추가
fileMenu.add_command(label="종료", command=func_exit)


imageMenu1 = Menu(mainMenu, tearoff=0)
imageMenu2 = Menu(imageMenu1, tearoff=0)
mainMenu.add_cascade(label="이미지 변환", menu=imageMenu1)
imageMenu1.add_cascade(label="색상 조정", menu=imageMenu2, state=tk.DISABLED)
imageMenu1.add_separator()
imageMenu1.add_command(label="확대", command=func_zoomin, state=tk.DISABLED)
imageMenu1.add_command(label="축소", command=func_zoomout, state=tk.DISABLED)
imageMenu1.add_separator()
imageMenu1.add_command(label="상하 반전", command=func_mirror1, state=tk.DISABLED)
imageMenu1.add_command(label="좌우 반전", command=func_mirror2, state=tk.DISABLED)
imageMenu1.add_separator()
imageMenu1.add_command(label="회전", command=func_rotate, state=tk.DISABLED)

imageMenu2.add_command(label="밝게", command=func_bright, state=tk.DISABLED)
imageMenu2.add_command(label="어둡게", command=func_dark, state=tk.DISABLED)
imageMenu2.add_separator()
imageMenu2.add_command(label="선명하게", command=func_clear, state=tk.DISABLED)
imageMenu2.add_command(label="탁하게", command=func_unclear, state=tk.DISABLED)
imageMenu2.add_separator()
imageMenu2.add_command(label="색조 조절", command=func_hue, state=tk.DISABLED)
imageMenu2.add_command(label="흑백이미지", command=func_bw, state=tk.DISABLED)

imageMenu3 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="이미지 효과", menu=imageMenu3)
imageMenu3.add_command(label="흐리게", command=func_blur, state=tk.DISABLED)
imageMenu3.add_command(label="더 흐리게", command=func_adblur, state=tk.DISABLED)
imageMenu3.add_command(label="가우시안", command=func_gausblur, state=tk.DISABLED)
imageMenu3.add_command(label="동작", command=func_motoinblur, state=tk.DISABLED)
imageMenu3.add_command(label="방사형 흐림효과", command=func_rotationblur, state=tk.DISABLED)
imageMenu3.add_separator()
imageMenu3.add_command(label="확산", command=func_Spread, state=tk.DISABLED)
imageMenu3.add_command(label="굴절", command=func_swirl, state=tk.DISABLED)
imageMenu3.add_separator()
imageMenu3.add_command(label="흑백 가장자리", command=func_edge, state=tk.DISABLED)
imageMenu3.add_command(label="엠보스", command=func_emboss, state=tk.DISABLED)
imageMenu3.add_command(label="석고", command=func_shade, state=tk.DISABLED)
imageMenu3.add_command(label="스케치", command=func_sketch, state=tk.DISABLED)


# 배경이미지
backgroundImage = PhotoImage(file="./images/bg.png")
bgLabel = Label(w, image=backgroundImage)
bgLabel.place(x=0, y=0)

# 빈 이미지 출력
photo = PhotoImage()
pLabel = Label(w, image=photo)
pLabel.place(x=0, y=0)



w.mainloop()
