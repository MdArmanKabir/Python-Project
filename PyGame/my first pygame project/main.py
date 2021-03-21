import pygame

pygame.init()
display_width = 700
display_height = 500
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("First pygame")
bg = pygame.image.load('pics//bg.png')
weaponsound = pygame.mixer.Sound('sound//weaponsound.wav')
hitSound = pygame.mixer.Sound('sound//hit.wav')
music = pygame.mixer.music.load('sound//theme.wav')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()


class Player:

    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.player_val = 5
        self.is_jump = False
        self.left = False
        self.right = False
        self.standing = True
        self.jump_val = 10
        self.walk_count = 0
        self.health=3
        self.death=False
        self.hitbox = (self.x + 20, self.y + 10, 64, 80)
        self.walk_right = [pygame.image.load('pics//NR2.png'), pygame.image.load('pics//NR3.png'),
                           pygame.image.load('pics//NR1.png')]

        self.walk_left = [pygame.image.load('pics//NL2.png'), pygame.image.load('pics//NL3.png'),
                          pygame.image.load('pics//NL1.png')]

        self.jump_pic = [pygame.image.load('pics//NL4.png'), pygame.image.load('pics//NR4.png')]
        self.death_pic=pygame.image.load('pics//Nd.png')

    def draw(self, win):
        if not self.death:

            if self.walk_count + 1 >= 8:
                self.walk_count = 0

            if not self.standing:
                if not self.is_jump:
                    if self.right:
                        win.blit(self.walk_right[self.walk_count // 4],
                                 (self.x, self.y, self.width, self.height))
                        self.walk_count += 1

                    elif self.left:
                        win.blit(self.walk_left[self.walk_count // 4],
                                 (self.x, self.y, self.width, self.height))
                        self.walk_count += 1
                else:
                    if self.right:
                        win.blit(self.jump_pic[1], (self.x, self.y, self.width, self.height))
                    else:
                        win.blit(self.jump_pic[0], (self.x, self.y, self.width, self.height))

            else:
                if self.left:
                    win.blit(self.walk_left[2], (self.x, self.y, self.width, self.height))
                else:
                    win.blit(self.walk_right[2], (self.x, self.y, self.width, self.height))
            self.hitbox = (self.x + 20, self.y + 10, 64, 80)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        else:
            win.blit(self.death_pic, (self.x, self.y, self.width, self.height))


    def movement(self, right_movement_key, left_movement_key, jump_key):
        if not self.death:
            if keys[right_movement_key] and self.x < (display_width - 85):
                self.right = True
                self.left = False
                self.standing = False
                self.x += self.player_val

            elif keys[left_movement_key] and self.x > -25:
                self.left = True
                self.right = False
                self.standing = False
                self.x -= self.player_val
            else:
                self.standing = True
                self.walk_count = 0

            if not self.is_jump:
                if keys[jump_key]:
                    self.is_jump = True
            else:
                if self.jump_val >= -10:
                    self.y -= int((self.jump_val * abs(self.jump_val)) * 0.5)
                    self.jump_val -= 1
                else:
                    self.jump_val = 10
                    self.is_jump = False

    def hit(self):
        self.is_jump=False
        self.jump_val=10
        self.x=0
        self.y=410
        self.walk_count=0

        if self.health-1 >0:
            # hitSound.play()
            self.health-=1
            
        else:
            self.death=True

        pass


class Weapons:
    def __init__(self, x, y, width, height, facing):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.facing = facing
        self.weapon_vel = 10 * facing
        self.hitbox = (self.x + 3, self.y + 2, 32, 32)

    def draw(self, win):
        win.blit(pygame.image.load('pics//s2.png'), (self.x, self.y, self.width, self.height,))
        self.hitbox = (self.x + 3, self.y + 2, 32, 32)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class Enemy:
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = (self.x, self.end)
        self.vel = 8
        self.walk_count = 0
        self.health = 10
        self.hitbox = (self.x + 20, self.y + 10, 64, 80)
        self.death = False
        self.walk_right = [pygame.image.load('pics//SR2.png'), pygame.image.load('pics//SR3.png'),
                           pygame.image.load('pics//SR1.png')]
        self.walk_left = [pygame.image.load('pics//SL2.png'), pygame.image.load('pics//SL3.png'),
                          pygame.image.load('pics//SL1.png')]
        self.death_pic = pygame.image.load('pics//Sd.png')

    def movement(self):
        if self.vel > 0:
            if self.x < self.end:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

    def draw(self, win):
        if not self.death:
            self.movement()
            if self.walk_count + 1 >= 8:
                self.walk_count = 0
            if self.vel > 0:
                win.blit(self.walk_right[self.walk_count // 4], (self.x, self.y, self.width, self.height))
                self.walk_count += 1
            else:
                win.blit(self.walk_left[self.walk_count // 4], (self.x, self.y, self.width, self.height))
                self.walk_count += 1

            self.hitbox = (self.x + 20, self.y + 10, 64, 80)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 12, self.hitbox[1] - 10, 50, 8))
            pygame.draw.rect(win, (0, 255, 0),
                             (self.hitbox[0] + 12, self.hitbox[1] - 10, 50 - (5 * (10 - self.health)), 8))
        else:
            win.blit(self.death_pic, (self.x, self.y, self.width, self.height))

    def hit(self):
        hitSound.play()
        if self.health - 1 > 0:
            self.health -= 1
        else:
            self.death = True


def redraw():
    win.blit(bg, (0, 0))
    player.draw(win)
    for playerWeapon in playerWeapons:
        playerWeapon.draw(win)
    for enemyWeapon in enemyWeapons:
        enemyWeapon.draw(win)
    enemy.draw(win)
    text = font.render('Score ' + str(score), 1, (0, 0, 0))
    win.blit(text, (570, 10))
    if not player.death:
        text = font.render('Life ' + str(player.health), 1, (0, 0, 0))
        win.blit(text, (10, 10))
    else:
        text = font.render('Death', 1, (0, 0, 0))
        win.blit(text, (10, 10))

    pygame.display.update()


player = Player(330, 413, 64, 64)

enemy = Enemy(65, 409, 64, 64, 600)
font = pygame.font.SysFont('comicsans', 30, True)
#font_p = pygame.font.SysFont('comicsans', 30, True)
playerWeapons = []
enemyWeapons=[]
shoot_time = 0
score = 0
gameLoop = True
while gameLoop:
    clock.tick(30)
    if shoot_time > 0:
        shoot_time += 1
    if shoot_time > 20:
        shoot_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False


    for playerWeapon in playerWeapons:
        if 700 > playerWeapon.x > 55:
            playerWeapon.x += playerWeapon.weapon_vel
        else:
            playerWeapons.pop(playerWeapons.index(playerWeapon))
        if not enemy.death:
            if playerWeapon.hitbox[1] + playerWeapon.hitbox[3] > enemy.hitbox[1] and playerWeapon.hitbox[1] < enemy.hitbox[1] + \
                    enemy.hitbox[
                        3]:
                if playerWeapon.hitbox[0] + playerWeapon.hitbox[2] > enemy.hitbox[0] and playerWeapon.hitbox[0] < enemy.hitbox[0] + \
                        enemy.hitbox[2]:
                    score += 1
                    enemy.hit()
                    playerWeapons.pop(playerWeapons.index(playerWeapon))

    for enemyWeapon in enemyWeapons:
        if 700 > enemyWeapon.x > 55:
            enemyWeapon.x += enemyWeapon.weapon_vel
        else:
            enemyWeapons.pop(enemyWeapons.index(enemyWeapon))
        if not player.death:
            if enemyWeapon.hitbox[1] + enemyWeapon.hitbox[3] > player.hitbox[1] and enemyWeapon.hitbox[1] < player.hitbox[1] + \
                    enemy.hitbox[
                        3]:
                if enemyWeapon.hitbox[0] + enemyWeapon.hitbox[2] > player.hitbox[0] and enemyWeapon.hitbox[0] < player.hitbox[0] + \
                        player.hitbox[2]:
                    score += 1
                    player.hit()
                    enemyWeapons.pop(enemyWeapons.index(enemyWeapon))

    if not enemy.death and not player.death:
        if player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1] and player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[
            3]:
            if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + \
                    enemy.hitbox[2]:

                player.hit()

    keys = pygame.key.get_pressed()
    right = pygame.K_RIGHT
    left = pygame.K_LEFT
    jump = pygame.K_UP
    player.movement(right, left, jump)

    if keys[pygame.K_SPACE] and shoot_time == 0:
        if player.left:
            facing = -1
        else:
            facing = 1
        if len(playerWeapons) < 2:
            weaponsound.play()
            playerWeapons.append(Weapons(player.x + player.width // 2, player.y + player.height // 2, 10, 10, facing))

            shoot_time = 1

    if enemy.path[0] == enemy.x:

        if len(enemyWeapons) < 2:
            weaponsound.play()
            enemyWeapons.append(Weapons(enemy.x + enemy.width // 2, enemy.y + enemy.height // 2, 10, 10,1))

            shoot_time = 1
    if enemy.x==601:
        if len(enemyWeapons) < 2:
            enemyWeapons.append(Weapons(enemy.x + enemy.width // 2, enemy.y + enemy.height // 2, 10, 10, -1))

            shoot_time = 1
    #pygame.time.delay(100)
    print(enemy.x)
    redraw()

pygame.quit()
