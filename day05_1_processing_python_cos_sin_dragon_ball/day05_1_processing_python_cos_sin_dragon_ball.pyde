# day05_1_processing_python_cos_sin_dragon_ball
# B某：學 cos() sin() 有用嗎？
# 買冬瓜cos(60) 西瓜sin(30)嗎？
# 在大學3D電腦圖學很有用
size(400, 400) # 視窗大小 400x400, 正中心(200,200)
ellipse(200, 200, 300, 300) # 圓 正中心(200, 200) 圓的大小300x300
for i in range(7): # 七龍珠有7個龍珠
    a = (PI*2/7)*i # 對應的角度a是1/7個圓 * i
    ellipse(200+150*cos(a), 200+150*sin(a), 80, 80) 
    # 畫出 80x80 的小圓
    # 圓心 200 半徑 150 x座標對應 cos(a)
    # 圓心 200 半徑 150 y座標對應 sin(a)
    
