# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:16:21 2026

@author: user
"""
# day08_4_spyder_face_detect_hat

import cv2
import numpy as np

# 讀人臉模型
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# 讀帽子（含透明 alpha）
hat = cv2.imread('hat.png', cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        
        # ====== 帽子大小（依臉縮放）======
        hat_width = w
        hat_height = int(hat.shape[0] * (hat_width / hat.shape[1]))

        resized_hat = cv2.resize(hat, (hat_width, hat_height))

        # ====== 帽子位置 ======
        y1 = y - hat_height
        y2 = y
        x1 = x
        x2 = x + hat_width
        
        # ====== 邊界處理（關鍵） ======
        if y1 < 0:
            resized_hat = resized_hat[-y1:, :, :]
            y1 = 0
        
        if x1 < 0:
            resized_hat = resized_hat[:, -x1:, :]
            x1 = 0
        
        if x2 > frame.shape[1]:
            resized_hat = resized_hat[:, :frame.shape[1]-x1, :]
            x2 = frame.shape[1]
        
        if y2 > frame.shape[0]:
            resized_hat = resized_hat[:frame.shape[0]-y1, :, :]
            y2 = frame.shape[0]
            
        # ====== 分離 alpha 通道 ======
        if resized_hat.shape[2] == 4:
            hat_rgb = resized_hat[:, :, :3]
            alpha = resized_hat[:, :, 3] / 255.0
        else:
            continue

        # ====== 疊加帽子 ======
        for c in range(3):
            frame[y1:y2, x1:x2, c] = (
                alpha * hat_rgb[:, :, c] +
                (1 - alpha) * frame[y1:y2, x1:x2, c]
            )

    cv2.imshow("Hat Filter", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()