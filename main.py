#Pygame Import
import pygame
pygame.init()

#CONSTANTS
BLACK = (0  , 0  , 0 )
WHITE = (255, 255, 255)
GREEN = (0 , 255 , 0 )
RED =   (255 ,  0 , 0)
 
#Window 
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
#End Loop
done = False
 
#Refresh rate
clock = pygame.time.Clock()

# --- Square ---

#Position
rect_x = 50
rect_y = 50

#Speed
rect_change_x = 5
rect_change_y = 5

# --- Paddle ---

#Position 
paddle_x =  25
paddle_y =  350

#Speed
paddle_change_y = 5

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    #Background color
    screen.fill(BLACK)

    # --- Square ---
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 35, 35])
    rect_x += rect_change_x
    rect_y += rect_change_y

    #Bounce
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0: 
        rect_change_x = rect_change_x * -1

    # --- Paddle --- 
    pygame.draw.rect(screen, WHITE, [paddle_x, paddle_y, 15, 110])

    #Controls
    keys = pygame.key.get_pressed()
    paddle_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * paddle_change_y

    #Refresh Screen
    pygame.display.flip()
 
    #FPS
    clock.tick(60)
 
#Close Game
pygame.quit()
