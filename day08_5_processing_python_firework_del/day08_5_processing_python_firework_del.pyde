# day08_5_processing_python_firework_del
# 想法來自昨天 day07_7_processing_python_friework_life_random
# 想了解 del 的意思 

a = [10,20,30,40] # 設定陣列的值

def setup(): # 設定的函式
    size(600,100)
    frameRate(1) # 每秒畫 draw()1次
    
def draw():
    background(0)
    # for i in range(len(a)):# 迴圈，把每個 a[i]走一次 
    for i in range(len(a)-1,-1,-1):
        fill(255) # 白色的方塊
        rect(i*80,0,80,80)
        fill(255,0,0) # 紅色的字
        text(a[i],i*80+40,40)
        a[i] -= 1 # 數值慢慢地減少
        if a[i] < 0: del a[i] # 要把值變成0的刪掉
        
def mousePressed(): # mouse 每按一秒，就增加1格
    a.append(int(random(5,30))) # 用 append() 加1格數值
