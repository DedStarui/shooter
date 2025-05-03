from pygame import*
from random import randint
window = display.set_mode((700, 500))
display.set_caption("shooter")
background = transform.scale(image.load("space.jpg"), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 633:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet2.png", self.rect.centerx, self.rect.top, 110, 110, 8)
        bullets.add(bullet)



player = Player("player.png", 300, 400, 65, 65, 12)
monsters = sprite.Group()
font.init()
font1 = font.Font(None, 36)
lost = 0
text_lose = font1.render("Пропущено" + str(lost), 1, (255, 255, 255))


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(10, 690)
            self.rect.y = 0
            lost += 1

class Bullet(GameSprite):
    def update(self):
        
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        
for i in range(1, 10):
    monster = Enemy("enemy.png", randint(70, 670), 500, 65, 65, randint(3, 5))
    monsters.add(monster)

bullets = sprite.Group()



game = True
game_finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    if not game_finish:
        window.blit(background, (0 , 0))
        window.blit(text_lose, (50, 50) )
        monsters.draw(window)
        monsters.update()
        player.reset()
        player.update()
        display.update()

        
    time.delay(30)
        
