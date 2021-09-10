import pygame

# Setup
pygame.init()

# Colors
color_black = (0  , 0  , 0 )
color_white = (255, 255, 255)
 
# Window 
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
fps = 60

# --- Ball ---

# Position
rect_x = 50
rect_y = 50

# Speed
rect_change_x = 5
rect_change_y = 5

# --- Paddle 1 ---

# Position 
paddle1_x =  25
paddle1_y =  200

# Speed
paddle1_change_y = 5

# --- Paddle 2 ---

# Position 
paddle2_x =  655
paddle2_y =  200

# Speed
paddle2_change_y = 5

# -------- Main Program Loop -----------
while True:
    clock.tick(fps)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit
 
    # Background color
    screen.fill(color_black)

    # --- Ball ---
    pygame.draw.rect(screen, color_white, [rect_x, rect_y, 35, 35])
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Bounce
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0: 
        rect_change_x = rect_change_x * -1

    # --- Paddle 1 --- 
    pygame.draw.rect(screen, color_white, [paddle1_x, paddle1_y, 15, 110])

    # Controls
    keys = pygame.key.get_pressed()
    paddle1_y += (keys[pygame.K_s] - keys[pygame.K_w]) * paddle1_change_y

    # Clamp Paddle to Play Area
    if paddle1_y < 0:
        paddle1_y = 0
    if paddle1_y > 400:
        paddle1_y = 400

    # --- Paddle 2 --- 
    pygame.draw.rect(screen, color_white, [paddle2_x, paddle2_y, 15, 110])

    # Controls
    keys = pygame.key.get_pressed()
    paddle2_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * paddle2_change_y

    # Clamp Paddle to Play Area
    if paddle2_y < 0:
        paddle2_y = 0
    if paddle2_y > 400:
        paddle2_y = 400
      
    # Refresh Screen
    pygame.display.flip()
