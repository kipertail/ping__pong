from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, pos_x, pos_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y 
        self.direction = "left"

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y < 700:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 150:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 150:
            self.rect.y += self.speed

    def fire(self):
        bullet = Bullet("bullet.png", 5, self.rect.centerx, self.rect.top, 15, 20)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        if not finish:
            self.rect.y += self.speed
            global lost
            if self.rect.y > win_height:
                self.rect.y = -40
                self.rect.x = random.randint(0, win_width - ufo_size_x)
                self.speed = random.randint(1, 4)
                lost +=1
        else:
            self.kill()


# Параметры окна
background_color = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
window.fill(background_color)



racket_left = Player('racket.png', 4, 30, 200, 50, 150)
racket_right = Player('racket.png', 4, 620, 200, 50, 150)
ball = Enemy('tenis_ball.png', 4, 200, 200, 50, 50)

# Игровой цикл
FPS = 60
clock = time.Clock()
run = True
finish = False



while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        

    if not finish:
        window.fill(background_color)
        racket_left.update_left()
        racket_right.update_right()

        ball.reset()
        racket_left.reset()
        racket_right.reset()

    clock.tick(FPS)
    display.update()