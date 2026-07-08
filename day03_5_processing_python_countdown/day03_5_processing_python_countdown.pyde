#day03_5_processing_python_countdown
# 修改自 day03_4_processing_python_countdow
# 倒數計時，先把時間印出來
target = 0 # 目標時間
def setup(): # 設定函式
    global target 
    size(500, 200) # 視窗大小
    mm = minute() # 分鐘(現在的時間)
    ss = second() # 秒鐘(現在的時間)
    target = (mm+5)*60 + ss # 所需的target目標時間
    
def draw(): # 畫圖的函式
    background(0) # 背景黑色
    textSize(150) # 字很大 150號字
    remain = target - minute()*60 - second() # 剩下的秒數
    mm = remain // 60 # 分鐘
    ss = remain % 60 # 秒鐘
    text( nf(mm, 2) + ":" + nf(ss, 2), 80, 150) # 接成數字 / str 轉換字串 / nf(,) 補零
