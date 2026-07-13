# day06_2_colab_wedcam_javascript_python.py
from IPython.display import display, Javascript
from google.colab.output import eval_js
import numpy as np
import cv2
from base64 import b64decode

# JS 取得攝影機畫面
def take_photo():
    js = Javascript('''
        async function takePhoto() {
          const div = document.createElement('div');
          const video = document.createElement('video');
          const stream = await navigator.mediaDevices.getUserMedia({video: true});

          document.body.appendChild(div);
          div.appendChild(video);
          video.srcObject = stream;
          await video.play();

          await new Promise(resolve => setTimeout(resolve, 1000));

          const canvas = document.createElement('canvas');
          canvas.width = video.videoWidth;
          canvas.height = video.videoHeight;
          canvas.getContext('2d').drawImage(video, 0, 0);

          stream.getTracks().forEach(track => track.stop());
          div.remove();

          return canvas.toDataURL('image/jpeg');
        }
    ''')
    display(js)
    data = eval_js('takePhoto()')
    binary = b64decode(data.split(',')[1])
    return binary

# 拍照
image_bytes = take_photo()

# 轉成 OpenCV 圖片
image_np = np.frombuffer(image_bytes, dtype=np.uint8)
frame = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

# 顯示圖片
from matplotlib import pyplot as plt
plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
plt.axis('off')

for i in range(5):  # 拍5張
    image_bytes = take_photo()
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    frame = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()