# day07_11_processing_python_gemini_code_tetris
# gemini:想要寫一個 Processing 的 Python Mode 的程式，想要模仿製作"俄羅斯方塊"的小遊戲，請給我程式
# 俄羅斯方塊 (Tetris) - Processing Python Mode
import random

# 遊戲視窗與網格設定
GRID_W = 10
GRID_H = 20
BLOCK_SIZE = 30

# 網格資料（0 代表空，其他數字代表顏色）
grid = [[0 for _ in range(GRID_W)] for _ in range(GRID_H)]

# 七種方塊的形狀定義 (以 4x4 或 3x3 矩陣表示)
SHAPES = [
    [[1, 1, 1, 1]], # I
    [[1, 1, 1], [0, 1, 0]], # T
    [[1, 1, 1], [1, 0, 0]], # L
    [[1, 1, 1], [0, 0, 1]], # J
    [[1, 1], [1, 1]], # O
    [[1, 1, 0], [0, 1, 1]], # Z
    [[0, 1, 1], [1, 1, 0]]  # S
]

COLORS = [
    (0, 0, 0),       # 背景色
    (0, 255, 255),   # I: 青色
    (128, 0, 128),   # T: 紫色
    (255, 165, 0),   # L: 橘色
    (0, 0, 255),     # J: 藍色
    (255, 255, 0),   # O: 黃色
    (255, 0, 0),     # Z: 紅色
    (0, 255, 0)      # S: 綠色
]

# 當前方塊狀態
current_shape = None
current_color_idx = 0
current_x = 0
current_y = 0

score = 0
game_over = False
drop_interval = 30 # 控制下落速度（幀數）

def setup():
    size(GRID_W * BLOCK_SIZE + 150, GRID_H * BLOCK_SIZE) # 右邊留 150px 顯示分數
    frameRate(60)
    new_piece()

def draw():
    global current_y, game_over
    background(40)
    
    if not game_over:
        # 自動下落邏輯
        if frameCount % drop_interval == 0:
            if not move(0, 1):
                freeze_piece()
                clear_lines()
                new_piece()
    
    draw_grid()
    draw_current_piece()
    draw_side_panel()

# 生成新方塊
def new_piece():
    global current_shape, current_color_idx, current_x, current_y, game_over
    current_color_idx = random.randint(1, len(SHAPES))
    current_shape = SHAPES[current_color_idx - 1]
    
    # 初始位置置中靠頂
    current_x = GRID_W // 2 - len(current_shape[0]) // 2
    current_y = 0
    
    # 如果一出生就碰撞，代表遊戲結束
    if check_collision(current_shape, current_x, current_y):
        game_over = True

# 繪製已固定的網格
def draw_grid():
    stroke(60)
    for r in range(GRID_H):
        for c in range(GRID_W):
            val = grid[r][c]
            fill(*COLORS[val])
            rect(c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

# 繪製當前控制的方塊
def draw_current_piece():
    if current_shape and not game_over:
        fill(*COLORS[current_color_idx])
        stroke(255)
        for r in range(len(current_shape)):
            for c in range(len(current_shape[r])):
                if current_shape[r][c]:
                    rect((current_x + c) * BLOCK_SIZE, (current_y + r) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

# 繪製右側資訊欄
def draw_side_panel():
    fill(255)
    textSize(20)
    text("SCORE", GRID_W * BLOCK_SIZE + 20, 50)
    textSize(30)
    text(str(score), GRID_W * BLOCK_SIZE + 20, 90)
    
    if game_over:
        fill(255, 0, 0)
        textSize(24)
        text("GAME OVER", GRID_W * BLOCK_SIZE + 10, 200)

# 碰撞偵測
def check_collision(shape, nx, ny):
    for r in range(len(shape)):
        for c in range(len(shape[r])):
            if shape[r][c]:
                grid_x = nx + c
                grid_y = ny + r
                # 檢查是否超出邊界
                if grid_x < 0 or grid_x >= GRID_W or grid_y >= GRID_H:
                    return True
                # 檢查是否與已有方塊重疊
                if grid_y >= 0 and grid[grid_y][grid_x] != 0:
                    return True
    return False

# 移動方塊
def move(dx, dy):
    global current_x, current_y
    if not check_collision(current_shape, current_x + dx, current_y + dy):
        current_x += dx
        current_y += dy
        return True
    return False

# 旋轉方塊 (矩陣順時針旋轉 90 度)
def rotate_piece():
    global current_shape
    # Python 矩陣旋轉技巧
    rotated = [list(x) for x in zip(*current_shape[::-1])]
    
    # 檢查旋轉後是否會碰撞，如果不會才允許旋轉
    if not check_collision(rotated, current_x, current_y):
        current_shape = rotated

# 將方塊固定到網格中
def freeze_piece():
    for r in range(len(current_shape)):
        for c in range(len(current_shape[r])):
            if current_shape[r][c]:
                if current_y + r >= 0:
                    grid[current_y + r][current_x + c] = current_color_idx

# 消除滿行
def clear_lines():
    global grid, score
    lines_cleared = 0
    # 從最後一行往上檢查
    new_grid = [row for row in grid if any(val == 0 for val in row)]
    lines_cleared = GRID_H - len(new_grid)
    
    # 補足被消除的行數（在頂部加上空行）
    if lines_cleared > 0:
        for _ in range(lines_cleared):
            new_grid.insert(0, [0 for _ in range(GRID_W)])
        grid = new_grid
        score += lines_cleared * 100

# 鍵盤控制
def keyPressed():
    if game_over:
        return
        
    if keyCode == LEFT:
        move(-1, 0)
    elif keyCode == RIGHT:
        move(1, 0)
    elif keyCode == DOWN:
        move(0, 1)
    elif keyCode == UP:
        rotate_piece()
    elif key == ' ': # 空白鍵直接到底 (Hard Drop)
        while move(0, 1):
            pass
        freeze_piece()
        clear_lines()
        new_piece()
