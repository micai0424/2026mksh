# day06_4_processing_python_friework_mousePressed_many
# 修改自 day06_3_processing_python_friework_gravity_20
# 想做出可以互動的煙火，而且 mouse 可點很多次
def setup():
    size(500, 500)
    
x, y = [], [] # 一開始的座標
vx, vy = [], [] # 一開始也沒有速度
gx, gy = 0, 0.0098 # 加速度
N = 0 # 現在要有幾顆火花?

def draw():
    background(0)
    fill(79, 211, 100)
    ellipse(mouseX, mouseY, 10, 10)
    for i in range(N):
        ellipse(x[i], y[i], 10, 10)
        x[i] += vx[i]
        y[i] += vy[i]
        vx[i] += gx
        vy[i] += gy
def mousePressed(): # mouse按下去
    global x, y, vx, vy, N 
    x += [mouseX]*20
    y += [mouseY]*20
    vx += [2*cos(PI*2/20*i)for i in range(20)]
    vy += [2*sin(PI*2/20*i)for i in range(20)]
    N += 20 # N 這裡有修改變數 N要記得用global
    
    
