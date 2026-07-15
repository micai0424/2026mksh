import cv2

# 開啟 webcam（0 = 預設鏡頭）
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("無法讀取畫面")
        break

    cv2.imshow("Webcam", frame)

    # 按 q 離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()