# day06_01_spyder_opencv_captgure.py
#  從 Chat GPT 得到的程式
# 修改自 day04_7_processing_java_vedio_library_Capture_start_read
import cv2

# 開啟第一台攝影機 (0 = 預設鏡頭)
cap = cv2.VideoCapture(0) # 0:第一台 1:第二台...

# 設定畫面大小、解析度 (對應 size(640,480))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 視訊寬度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 視訊高度

while True:
  # 迴圈一直跑，直到有 break 跳開結束
    ret, frame = cap.read()  # 對應 cam.read()

    if not ret: # 若沒有成功，就離開
        break

    # 顯示畫面 (對應 image(cam,0,0))
    cv2.imshow("Camera", frame)
    
    if cv2.waitKey(1) == 27: # 按Esc 離開(改成按 Esc 離開)
        break # waitKey(等多久? 單位 ms)
    
    # 按 q 離開
    # if cv2.waitKey(1) & 0xFF == ord('q'):
      #  break

# 關閉
cap.release() # 把 camera 正確關閉(收尾很重要)
cv2.destroyAllWindows() # 把剛剛開啟的 OpenCV 視窗全部關掉

