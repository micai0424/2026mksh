#day02_8b_processing_pthon_array
img = None
img2 = None

a =[
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
] #二維矩陣的定義

def setup(): 
    size(500,300)
    global img, img2
    img = loadImage("cat.png")
    img2 = loadImage("cat2.png")  
    
def draw():
    background(255)
    for i in range(3):
        for j in range(5):
            if a[i][j]==1:
                image(img, j*100, i*100, 100, 100)
            elif a[i][j]==2:
                image(img2, j*100, i*100, 100, 100)

def mousePressed():
    i = mouseY //100
    j = mouseX //100
    if 0 <= i <3 and 0 <= j <5:
        a[i][j] = (a[i][j] + 1) % 3
