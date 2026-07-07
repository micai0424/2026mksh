//day02_3_processing_java_for_for_image
//練習用for迴圈
PImage img;
void setup() {
  size(500, 300);
  img = loadImage("cat.png");
} //要記得，把cat.png圖檔，拉入程式裡

void draw() {
  background(255);
  for(int i=0; i<3; i++) {
    for(int j=0; j<5; j++) {
      image(img, j*100, i*100, 100, 100);
    } //要小心 x座標是j, y座標是i
  }
}
