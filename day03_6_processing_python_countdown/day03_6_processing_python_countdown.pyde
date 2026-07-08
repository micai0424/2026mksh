#day03_6_processing_python_countdown
# 修改自 day03_5_processing_python_countdow
# 有時候變負數， 而且太快開始，而且不能暫停!
# (1) 小鹿：用 max()找最大值 max(負數, 0)
# (2) 鬧鐘要可以修改用 day03_3 的 mouseDragged 來滑動 
# (3) 要可以暫停
target = 0 # 目標時間
target0 = 0 # 現在設定、要倒數的秒數
def mouseDragged():
    global target0
    target0 -= mouseY -pmouseY 
    target0 = min(59, target0)
    target0 = max(0, target0)

def setup(): # 設定函式
    size(500, 200) # 視窗大小
    
play = False
def mousePressed(): # 右鍵用來開始、暫停
    global play
    if mouseButton==RIGHT: play = not play
        #target = minute()*60+ second()+target0
    
def draw(): # 畫圖的函式
    background(0) # 背景黑色
    textSize(150) # 字很大 150號字
    remain = target0 # max(target - minute()*60 - second(), 0) # 剩下的秒數
    mm = remain // 60 # 分鐘
    ss = remain % 60 # 秒鐘
    text( nf(mm, 2) + ":" + nf(ss, 2), 80, 150) # 接成數字 / str 轉換字串 / nf(,) 補零
