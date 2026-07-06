//day01_processing_java_eraser_mouseButton_LEFT_RIGHT_stroke_ellipse
//有橡皮擦的版本
void setup() {// 設定的函式
  size (500, 500);//視窗 500 X 500
  background(255);// 白色背景
}
void draw() {//畫圖的函示
//如果mouse按下去
  if(mousePressed && mouseButton==LEFT) {//mouse左鍵按下去
   stroke(255, 0, 0); //紅色的線
   line(mouseX, mouseY, pmouseX, pmouseY);
}
  if(mousePressed && mouseButton==RIGHT) { //mouse右鍵按下去
   noStroke();//不要畫線
   ellipse(mouseX, mouseY, 20, 20);//畫 20 X 20的圖, 蓋掉畫錯的圖
  }
}
