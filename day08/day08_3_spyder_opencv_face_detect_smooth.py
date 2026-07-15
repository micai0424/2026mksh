# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:59:42 2026

@author: user
"""
# day08_3_spyder_opencv_face_detect_smooth
# face detect 出來的人臉會有點抖動，為什麼？請問要怎麼改成每有抖動的版本？
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

# 初始化位置
prev_x, prev_y, prev_w, prev_h = 0, 0, 0, 0
alpha = 0.7  # 平滑程度（越大越穩，但越慢）

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # 平滑處理
        x = int(alpha * prev_x + (1 - alpha) * x)
        y = int(alpha * prev_y + (1 - alpha) * y)
        w = int(alpha * prev_w + (1 - alpha) * w)
        h = int(alpha * prev_h + (1 - alpha) * h)

        prev_x, prev_y, prev_w, prev_h = x, y, w, h

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Smooth Face", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()