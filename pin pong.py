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
    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 65:
            self.rect.x += self.speed

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

    clock.tick(FPS)
    display.update()