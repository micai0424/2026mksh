# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:40:04 2026

@author: user
"""

# day08_2_spyder_opencv_face_detection
# 我想在剛剛的程式碼延伸，希望能夠偵測到人臉，用一些線條或圓形，把臉框起來。
# 請問該怎麼做修改？

import cv2

# 讀取人臉模型（OpenCV 內建）
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("無法讀取畫面")
        break

    # 轉灰階（人臉偵測用）
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 偵測人臉
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # 畫框（矩形）
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 或畫圓（可選）
        center = (x + w//2, y + h//2)
        radius = w // 2
        #cv2.circle(frame, center, radius, (255, 0, 0), 2)

    cv2.imshow("Face Detection", frame)

    # ESC 離開
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()