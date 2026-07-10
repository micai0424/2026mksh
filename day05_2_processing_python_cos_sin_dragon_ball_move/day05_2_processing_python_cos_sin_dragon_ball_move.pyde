# day05_2_processing_python_cos_sin_dragon_ball_move
# 想讓7個龍珠 "轉動"
def setup(): 
    size(400, 400)
    
def draw():
    background(0)
    for i in range(7):# 七龍珠，跑7次迴圈
       # a = (PI*2/7)* i + mouseX/1000.0 # 轉動，是要增加角度
        a= (PI*2/7)*i + radians(frameCount)/5 #讓他自行轉動
        ellipse(200+150*cos(a), 200+150*sin(a), 80, 80)
