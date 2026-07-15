# day08_1_spyder_opencv_webcam
# 我們想在Spyder裡，使用OpenCV讀入webcam視訊鏡頭的畫面，即時更新。
# 要做哪些步驟？有哪些可能卡住的地方？
# 因為中文注音輸入法，會卡住q鍵，可以改ESC鍵的版本嗎
import cv2

# 開啟 webcam（0 = 預設鏡頭）
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("無法讀取畫面")
        break

    cv2.imshow("Webcam", frame)
    
    
    if cv2.waitKey(1)  == 27:
        break

    # 按 q 離開
   # if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

cap.release()
cv2.destroyAllWindows()