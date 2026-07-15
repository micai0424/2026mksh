# day07_7_processing_python_friework_life_random
# 修改自 day06_6_processing_python_friework_stroke_line_line
# 每個花火，都有自己的生命值
def setup():
    size(500, 500)
    
life = []
r, g, b = [], [], []
x, y = [], [] # 一開始的座標
vx, vy = [], [] # 一開始也沒有速度
gx, gy = 0, 0.0098 # 加速度
N = 0 # 現在要有幾顆火花?

def draw():
    global N
    background(0)
    ellipse(mouseX, mouseY, 10, 10)
    for i in range(N-1,-1,-1):
        fill(r[i], g[i], b[i]) # 加色彩的變數(隨機變色)
        # ellipse(x[i], y[i], 10, 10) # 不要只畫圓形
        stroke(r[i], g[i], b[i]) # 改成彩色線條
        strokeWeight(5) #設訂線條寬度
        line(x[i],y[i],x[i]+vx[i], y[i]+vy[i]) # 畫線到下一格位子
        x[i] += vx[i]
        y[i] += vy[i]
        vx[i] += gx
        vy[i] += gy
        line(x[i],y[i],x[i]+vx[i], y[i]+vy[i]) # 畫線到下下一格位子
        if life[i] > 0: life[i] -= 1 # 減掉1點生命值
        else:
            del life[i]
            del r [i]
            del g [i]
            del b[i]
            del x[i]
            del y[i]
            del vx[i]
            del vy[i]
            N -= 1
def mousePressed(): # mouse按下去
    global life,r, g, b, x, y, vx, vy, N
    life += [random(120,240)]*20 # 生命值介於2秒-7秒
    r += [random(256)]*20
    g += [random(256)]*20
    b += [random(256)]*20
    x += [mouseX]*20
    y += [mouseY]*20
    vx += [2*cos(PI*2/20*i)for i in range(20)]
    vy += [2*sin(PI*2/20*i)for i in range(20)]
    N += 20 # N 這裡有修改變數 N要記得用global
