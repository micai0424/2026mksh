# day05_5_processing_pythhon_firework_cos_sin
# 花火節煙火，先畫出 "從中心往外畫出20線"
def setup():
    size(500, 500) #視窗 500x500 中心(250,250)
def draw():
    background(22, 8, 64) #背景顏色 
    for i in range(20): 
        R = 20 + mouseX # 花火的爆炸半徑，是 20 + mouseX
        a = (PI*2/20)*i # 圓/7 * i 會有不同的角度
        line(250, 250, 250+R*cos(a),250+R*sin(a) ) 
        # 黑色的線，從中心(250, 250)往半徑R的大圈外面射出去
        stroke(145,115, 242) # 線條顏色
         
       
