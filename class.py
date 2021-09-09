import pygame 

#Setup
pygame.init()

#Window Settings
window_height = 800
window_width = 600
fps = 60
clock = pygame.time.Clock()

#Colours
black = (255, 255, 255)
white = (0  , 0  , 0  )  

#Window 
game_window = pygame.display.set_mode((window_height, window_width))
pygame.display.set_caption('Pong')

# --- Ball ---
class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.width = 35
        self.height = 35
        self.color = (0, 0, 0)

        def movement(self):
            self.x += self.change_x
            self.y += self.change_y
        
        def draw(self, game_window):
            pygame.draw.rect(game_window, self.color, [self.x, self.y], self.width, self.height)

class Paddle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_y = 0
        self.width = 35
        self.height = 35
        self.color = (0, 0, 0)

        def update(self):
            keys = pygame.key.get_pressed()
            self.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.change_y

            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > window_height:
                self.rect.bottom = window_height

        def draw(self, game_window):
            pygame.draw.rect(game_window, self.color, [self.x, self.y], self.width, self.height)



# -------- Main Program Loop -----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    Square = Ball()
    Square.x = 50
    Square.y = 50
    Square.change_x = 3
    Square.change_y = 3
    Square.color = [0, 0, 0]
    Square.draw(game_window)

    Player = Paddle()
    Player.x = 25
    Player.y = 350
    Player.change_y = 5
    Player.color = [0, 0, 0]
    Player.move()
    Player.draw(game_window)


    #Refresh Screen 
    pygame.display.update()