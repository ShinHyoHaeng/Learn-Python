
## Python 능력단위 과제: 미니 포토샵 프로그램 제작
# 함수 내용 참고: https://docs.wand-py.org/en/0.6.7/guide/effect.html

from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *


## 함수 정의 부분
# 이미지 준비
def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width) + "x" + str(height))

    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, width=width, height=height)
    paper = PhotoImage(width=width, height=height)
    canvas.create_image((width / 2, height / 2), image=paper, state="normal")

    blob = img.make_blob(format='RGB')
    for i in range(0, width):
        for k in range(0, height):
            r = blob[(i * 3 * width) + (k * 3) + 0]
            g = blob[(i * 3 * width) + (k * 3) + 1]
            b = blob[(i * 3 * width) + (k * 3) + 2]
            paper.put("#%02x%02x%02x" % (r, g, b), (k, i))

    canvas.pack()

# 이미지 열기
def func_open() :
    global window, canvas, paper, photo, photo2, oriX, oriY

    redFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"), ("모든 파일", "*.*")))
    photo = Image(filename=redFp)

    oriX = photo.width
    oriY = photo.height

    photo2 = photo.clone()
    newX = photo2.width
    newY = photo2.height

    displayImage(photo2, newX, newY)

# 다른 이름으로 이미지 저장
def func_save_as() :
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    if photo2 == None:
        return

    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*") ))
    savePhoto = photo2.convert("jpg")
    savePhoto.save(filename=saveFp.name)

# 프로그램 종료
def func_exit() :
    window.quit()
    window.destroy()

# 확대
def func_zoomin() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대배수", "확대할 배수를 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.clone()
    photo2.resize(int(oriX * scale), int(oriY * scale))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 축소
def func_zoomout() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소배수", "축소할 배수를 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.clone()
    photo2.resize(int(oriX / scale), int(oriY / scale))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 좌우 반전
def func_flip() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.flip()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 상하 반전
def func_flop() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.flop()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 회전
def func_rotate() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    photo2.clone()
    photo2.rotate(degree)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 밝기 조절
def func_brightness() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("밝기 조절", "값을 입력하세요(어둡게:0~100/밝게:100~200)", minvalue=0, maxvalue=200)
    photo2.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 선명도 조절
def func_clear() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("선명도 조절", "값을 입력하세요(흐리게:0~100/선명하게:100~200)", minvalue=0, maxvalue=200)
    photo2.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 흑백 효과
def func_bw() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2.clone()
    photo2.type = "grayscale"
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 되돌리기
def func_revert() :
    global window, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    photo2 = photo.clone()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 테두리
def func_border() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    color = askstring("테두리 색상 선택", "색상값을 입력하세요")
    b_width = askinteger("테두리 넓이 선택", "넓이값을 입력하세요", minvalue=0, maxvalue=10)
    b_height = askinteger("테두리 높이 선택", "높이값을 입력하세요", minvalue=0, maxvalue=10)
    photo2.clone()
    photo2.border(color, b_height, b_width)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 기울임 보정
def func_deskew() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("기울임 보정", "값을 입력하세요(0.0~1.0)", minvalue=0.0, maxvalue=1.0)
    photo2.clone()
    photo2.deskew(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 자르기
def func_crop() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    left = askinteger("이미지 자르기", "가로 시작점 값을 입력하세요", minvalue=0, maxvalue=250)
    top = askinteger("이미지 자르기", "세로 시작점 값을 입력하세요", minvalue=0, maxvalue=250)
    right = askinteger("이미지 자르기", "가로 범위를 입력하세요", minvalue=0, maxvalue=250)
    bottom = askinteger("이미지 자르기", "가로 시작점을 입력하세요", minvalue=0, maxvalue=250)
    photo2.clone()
    photo2.crop(left, top, right, bottom)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 흐림 효과
def func_blur() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    value1 = askinteger("기본 흐림 효과", "반경 값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    value2 = askinteger("기본 흐림 효과", "흐림 값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    photo2.clone()
    photo2.blur(radius=value1, sigma = value2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 가우시안 흐림 효과
def func_gb() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("가우시안 흐림 효과", "흐림 값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    photo2.clone()
    photo2.blur(sigma=value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 선명 효과
def func_sharpen() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    value1 = askinteger("선명 효과", "반경 값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    value2 = askinteger("선명 효과", "한계 값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    photo2.clone()
    photo2.sharpen(radius=value1, sigma=value2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 노이즈 반점 제거
def func_despeckle() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2.clone()
    photo2.despeckle()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 엣지 효과
def func_edge() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2.clone()
    photo2.transform_colorspace('gray')
    value = askinteger("엣지 효과", "반경 값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    photo2.edge(radius=value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 엠보스 효과
def func_emboss() :
    global window, canvas, paper, photo, photo2, oriX, oriY
    value1 = askinteger("엠보스 효과", "반경 값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    value2 = askinteger("엠보스 효과", "한계 값을 입력하세요(0~10)", minvalue=0, maxvalue=10)
    photo2.clone()
    photo2.transform_colorspace('gray')
    photo2.emboss(radius=value1, sigma=value2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


# 변수 선언 부분
window,canvas, paper = None, None, None
photo, photo2 = None, None
oriX,oriY = 0,0


# 메인 코드 부분
window = Tk()
window.geometry("250x250")

window.title("Simple Photoshop v.1.1")

mainMenu = Menu(window)
window.config(menu=mainMenu)

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)


# 메뉴 구성
fileMenu = Menu(mainMenu)
editMenu = Menu(mainMenu)
imageMenu = Menu(mainMenu)
filterMenu = Menu(mainMenu)
viewMenu = Menu(mainMenu)

# File(파일)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=func_open) # 이미지 열기
# fileMenu.add_command(label="Save", command=func_save) # 저장
fileMenu.add_command(label="Save As...", command=func_save_as) # 다른 이름으로 저장
fileMenu.add_command(label="Revert", command=func_revert) # 되돌리기
fileMenu.add_command(label="Exit", command=func_exit) # 프로그램 종료

# Edit(편집)
transformMenu = Menu(editMenu)
flipMenu = Menu(editMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Stroke",command=func_border) # 테두리
editMenu.add_cascade(label="Transform", menu=transformMenu)
transformMenu.add_command(label="Rotate", command=func_rotate) # 이미지 회전
transformMenu.add_command(label="Remove Skew", command=func_deskew) # 기울임 보정
editMenu.add_cascade(label="Flip", menu=flipMenu)
flipMenu.add_command(label="Flip Horizontal", command=func_flip) # 좌우 반전
flipMenu.add_command(label="Flip Vertical", command=func_flop) # 상하 반전

# Image(이미지)
mainMenu.add_cascade(label="Image", menu=imageMenu)
imageMenu.add_command(label="Greyscale", command=func_bw) # 흑백 효과
imageMenu.add_command(label="Brightness", command=func_brightness) # 밝기 조절
imageMenu.add_command(label="Clear", command=func_clear) # 선명도 조절
imageMenu.add_command(label="Crop", command=func_crop) # 자르기

# Filter(필터)
blurMenu = Menu(filterMenu)
noiseMenu = Menu(filterMenu)
mainMenu.add_cascade(label="Filter", menu=filterMenu)
filterMenu.add_cascade(label="Blur", menu=blurMenu)
blurMenu.add_command(label="Blur", command=func_blur) # 흐림 효과(기본)
blurMenu.add_command(label="Gaussian Blur", command=func_gb) # 가우시안 흐림 효과
filterMenu.add_command(label="Sharpen", command=func_sharpen) # 선명 효과
filterMenu.add_command(label="Despeckle", command=func_despeckle) # 노이즈 반점 제거
filterMenu.add_command(label="Edge", command=func_edge) # 엣지 효과
filterMenu.add_command(label="Emboss", command=func_emboss) # 엠보스 효과

# View(보기)
mainMenu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Zoom In", command=func_zoomin) # 확대
viewMenu.add_command(label="Zoom out", command=func_zoomout) # 축소


window.mainloop()

