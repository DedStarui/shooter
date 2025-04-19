from pygame import*
from random import randint
window = display.set_mode((700, 500))
display.set_caption("shooter")
background = transform.scale(image.load("space.jpg"), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
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
        if keys[K_d] and self.rect.x > 495:
            self.rect.x += self.speed
    def fire(self):
        pass

monsters = sprite.Group()
monsters.add(monster)
monsters.draw(window)
monsters.update()
lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(10, 690)
            self.rect.y = 0
            lost += 1


for i in range(1, 20):
    monster = Enemy("enemy.png", randint(10, 690), 510, randint(3, 8))
    monsters.add(monster)
