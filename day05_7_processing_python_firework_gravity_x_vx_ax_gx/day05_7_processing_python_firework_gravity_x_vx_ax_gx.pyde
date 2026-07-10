# day05_7_processing_python_firework_gravity_x_vx_ax_gx
# 物理大師(牛頓) F = ma 位置、速度、加速度
def setup():
    size(500, 500)
    
x, y = 0, 250 # 位置
vx, vy = 10, -10 # 速度
gx, gy = 0, 0.98 # 加速度(9.8老師縮小為0.98)
def draw():
    global x, y, vx, vy # 修改外來的全域變數
    # background(0) #先不調背景顏色，才能看到殘影
    stroke(255, 255,0)
    ellipse(x, y, 10, 10)
    x += vx # 位置會隨著"速度"改變
    y += vy
    vx += gx #數度會因為"加速度"而改變
    vy += gy
    
