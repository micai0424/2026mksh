# day05_6_processing_pythhon_firework_arrow
# 修改自 day05_5_processing_pythhon_firework_cos_sin
# 
def setup():
    size(500, 500) #視窗 500x500 中心(250,250)
def draw():
    background(0) #背景顏色 
    stroke(146, 115, 242) # 線條顏色
    for i in range(40): 
        R = 20 + mouseX # 花火的爆炸半徑，是 20 + mouseX
        a = (PI*2/40)*i # 圓/7 * i 會有不同的角度
        # line(250, 250, 250+R*cos(a),250+R*sin(a) ) 
        # 黑色的線，從中心(250, 250)往半徑R的大圈外面射出去
        line(250+(R-20)*cos(a), 250+(R-20)*sin(a), 250+R*cos(a), 250+R*sin(a))
        # 煙火的線條，從(R-20)距離，射到R距離(往外發出去) 
