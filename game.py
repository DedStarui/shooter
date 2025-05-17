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
        bullet = Bullet("bulleto.png", self.rect.centerx, self.rect.top, 110, 110, 15)
        bullets.add(bullet)

    def super_fire(self):
        super_bullet = SuperBullet("super_bullet.png", self.rect.centerx - 25, self.rect.top, 50, 50, 10)
        #super_bullets.add(super_bullet)



player = Player("player.png", 300, 400, 65, 65, 12)
monsters = sprite.Group()
font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 50)
font3 = font.Font(None, 50)
lose = font2.render("YOU LOOooOST!",1, (255, 0, 0))
win = font3.render("wow you won",1, (100, 0, 0))
lost = 0


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(10, 600)
            self.rect.y = -100
            lost += 1

class Bullet(GameSprite):
    def update(self):
        
        self.rect.y -= self.speed
        if self.rect.y < -10:
            self.kill()
        
for i in range(1, 7):
    monster = Enemy("enemy.png", randint(140, 520), -10, 65, 65, randint(3, 5))
    monsters.add(monster)
bullets = sprite.Group()
#super_bullets = sprite.Group()

score = 0
game = True
game_finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
            #elif e.key == K_r:
            #player.super_fire()

    if not game_finish:
        text_lose = font1.render("Пропущено" + str(lost), 1, (255, 255, 255))
        text_win = font1.render("Збито:" + str(score), 1, (255, 255, 255))
        window.blit(background, (0 , 0))
        window.blit(text_lose, (50, 50) )
        window.blit(text_win, (50, 75) )
        monsters.draw(window)
        bullets.draw(window)
        bullets.update()
        #super_bullets.update()
        #super_bullets.draw(window)
        monsters.update()
        player.reset()
        player.update()
        sprite_list = sprite.groupcollide(monsters, bullets, True, True)
        #super_hits = sprite.groupcollide(monsters, super_bullets, True, False)
        for c in sprite_list:
            score += 1
            monster = Enemy("enemy.png", randint(140, 520), -10, 65, 65, randint(3, 5))
            monsters.add(monster)

        if sprite.spritecollide(player, monsters, False) or lost >= 10:
            game_finish = True
            window.blit(lose, (250, 250))
        if score >= 20:
            game_finish = True
            window.blit(win, (250, 250))

        display.update()
        

        
    time.delay(27)
        


        
