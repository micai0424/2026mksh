# day04_4_processing_python_frameCount_
# 了解day4_3的frameCount是甚麼意思

def setup():
    size(400, 400)
    #frameRate(5) #讓 draw() 跑慢一點，1秒5次
  
# 如果想知道現在是第幾次執行void draw()要用t來數
t = 1 #第1行，宣告t變數
def draw():
    global t # 認識外來t
    background(0)
    textSize(100)
    textAlign(CENTER, CENTER)
    text(frameCount, 200, 100)
    
    text(t, 200, 200) # 試著畫出 t 的值
    t += 1 #每次結束時 t 會"加一"
    
    text(frameCount//60, 200, 300) #每秒60次，//60變秒
