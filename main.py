# 引入pygame模块 用cmd pip install pygame
import pygame;
# pygame 中的常量
from pygame.locals impport *
from sys import exit

# 设置游戏屏幕大小
# 主窗体实现
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


# 子弹类
class Bullt(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):  # 子弹图片及位置
        pygame.sprite.Sprite.__init__(self)  # 实现父类初始化方法
        self.image = bullet_img
        self.rect = self.image.get_rect()

        self.rect.midbottom = init_pos  # 子弹发射位置
        self.speed = 10

        def move(self):
            self.rect.top -= self.speed  # 每次调用方法就减速，相当于子弹向上移动


# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.imge = []  # 小飞机图片和飞机爆炸效果图，用列表存
        for i in range(len(player_rect)):
            self.imge.append(plane_img.subsurface(player_rect[i].convert_alpha())
            self.rect = player_rect[0]
            self.rect.topleft = init_pos  # 左上角坐标
            self.speed = 8
            self.bullets = pygame.spirte.Group()  # 定义飞机发射子弹的集合
            self.imge_index = 0
            self.is_hit = False  # 默认飞机没有被击中

            # 发射子弹

        def shoot(self, buttet_img):
            buttet = Bullt(buttet_img, self.rect.midtop)  # 传递子弹图片及发射位置
            self.bullet.add(buttet)  # 发射的子弹添加到创建的速度里

            # 飞机的向上移动
            def moveUp(self):
                if self.rect.top <= 0:  # 小于0超出边界
                    self.rect.top = 0
                else:
                    self.rect.top -= self.speed

        # 向下
        def moveDown(self):
            if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
                self.top = SCREEN_HEIGHT - self.rect.height  # 如果顶部大于主界面高减图片的高，证明飞机已经在最底部
            else:
                self.rect.top += self.speed

        # 向左
        def moveLeft(self):
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.rect.left -= self.speed

        # 向右
        def moveRight(self):
            if self.rect.left >= SCREEN_WIDTH - self.rect.width:
                self.rect.left = SCREEN_WIDTH - self.rect.width
            else:
                self.rect.left += self.speed


# 敌机
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_img, init_pos):  # 敌机初始化方法，敌机图片及击落时候图片和位置
        pygame.sprite.Sprite.__init__(self)  # 调用父类初始化方法

    self.image = enemy_img  # 设置图片
    self.rect = self.image.get_rect()  # 设置位置
    self.rect.topleft = init_pos
    self.down_imgs = enemy_down_imgs
    self.speed = 2
    self.down_imgs_index = 0

    def move(self):
        self.rect.top += self.speed

        def move(self):
            self.rect.top += speed


# 游戏界面设置
# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # pygame内置方法实现界面大小
pygame.display.set_caption('飞机大战')  # 设置名称
ic_launcher = pygame.image.load('resources/image/ic_launcher.png').convert_alpha()  # 插入图片，并使它透明
pygame.display.set_icon(ic_launcher)  # 设置icon,修改显示窗口图标
background = pygame.image.load("resources/image/background.png")  # 加载背景图
game_over = pygame.image.load('resources/image/gameover.png')  # 游戏结束画面
plane_img = pygame.image.load('resources/image/shoot.png')


def startGame():
    player_rect = []
    player_rect.append(pygame.Rect(0, 99, 100, 120))  # 获取图片所在位置
    player_rect.append(pygame.Rect(165, 360, 102, 126))  # 获取图片所在位置
    # 碰撞后飞机图片
    player_rect.append(pygame.Rect(165, 234, 102, 126))  # 获取图片所在位置
    player_rect.append(pygame.Rect(330, 498, 102, 126))  # 获取图片所在位置
    player_rect.append(pygame.Rect(330, 498, 102, 126))  # 获取图片所在位置
    player_rect.append(pygame.Rect(432, 624, 102, 126))  # 获取图片所在位置
    player_pos[200, 600]
    player = Player(plane_img, player_rect, player_pos)
    bullet_rect = pygame.Rect(1005, 987, 10, 21)
    bullet_img = plane_img.subsurface(bullet_rect)
    enemy1_rect = pygame.Rect(530, 612, 57, 43)
    enemy1_img = plane_img.subsurface(enemy1_rect)
    enemy1_down_ims = []
    enemy1_down_ims.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
    enemy1_down_ims.append(plane_img.subsurfacepygame.Rect(pygame.Rect(873, 697, 57, 43)))
    enemy1_down_ims.append(plane_img.subsurfacepygame.Rect(pygame.Rect(267, 296, 57, 43)))
    enemy1_down_ims.append(plane_img.subsurfacepygame.Rect(pygame.Rect(930, 697, 57, 43)))
    shoot_frequency = 0
    enemy_frequency = 0
    player_down_index = 16
    enemies1 = pygame.sprite.Group()
    enemies_down = pygame.sprite.Group()


# 游戏主循环
running = TURE
while running:
    screen.fill(0)
    screen.blit(background, (0, 0))
    # 生成子弹
    if not player.is_hit:
        if shoot_frequency % 15=0:
            player.shoot(bullet_img)
            shoot_frequency += 1
            if shoot_frequency >= 15
                shoot_frequency = 0
        for bullet in player.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                player.bullets.remove(bullet)
                player.bullets.draw(screen)
                if enemy_frequency % 50=0
                enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
            enemy1 = Enemy(enemy1_img, enemy1_down_ims, enemy1_pos)
        enemies1.add(enemy1)
    enemy_frequency += 1
if enemy_frequency >= 100:
    enemy_frequency = 0
for enemy in enemies1:
    enemy.move()
    if enemy.rect.top < 0:
        enemies1.remove(enemy)
    if pygame.sprite.collide_circle(enemy, player):
        enemies_down.add(enemy)
        enemies1.remove(enemy)
        player.is_hit = True
        break
        # 玩家飞机
    if not player.is_hit:
        screen.bit(player.imge[player.imge_index], player.rect)
        player.image_index = shoot_frequency // 8
    else:
        player.image_index = player_down_index // 8
        screen.blit(player.image[player.image_index], player.rect)
        player.image_index + 1
        if player_down_index > 47:
            running = False

        enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, True, 1)
        for enemy_down in enemies1_down:
            enemies_down.add(enemy_down)
        for enemy - down in enemies_down:
            if enemy_down.down_index > 7:
                enemies_down.remove(enemy_down)
                continue
                screen.blit(enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)
                enemy_down.down_index += 1
                enemies1.draw(screen)
pygame.display.update()  # 循环一次后更新一下屏幕
for event in pygame.event.get():
    if event.type=pygame.QUIT:  # 判断退出游戏
        pygame.quit()
        exit()
key_pressed = pygame.key.get_pressed()  # 获取键盘点击事件
if key_pressed[K_w] or key_pressed[K_UP]:  # 判断点击向上
    player.moveUp()

if key_pressed[K_s] or key_pressed[K_DOWN]:  # 判断点击向下
    player.moveDown()

if key_pressed[K_a] or key_pressed[K_LEFT]:  # 判断点击向左
    player.moveLeft()

if key_pressed[K_d] or key_pressed[K_RIGHT]:  # 判断点击向右
    player.moveRight()
startGame()

#游戏主循环结束后 游戏画面
screen.blit(game_over,(0,0)) #在0点 显示游戏结束图片
font=pygame.font.Font(None,48)#绘制分数
text=font.render('Score:'+str(score),Trut,(255,0,0))
text_rect=text.get_rect()
text_rect.centerx=screen.get_rect().centerx #横坐标
text_rect.centery=screen.get_rect().centery+24#纵坐标
screen.blit(text,text_rect#显示最终得分
#重新开始按钮
xtfont=pygame.font.SysFont('SimHei',30)#系统字体
textstart=xtfont.render('重新开始',True,(255,0,0))
text_rect=textstart.get_rect()
text_rect.centerx=screen.get_rect().centerx
text_rect.centery=screen.get_rect().centery+180
screen.blit(textstart,text_rect)
#排行榜
textstart=xtfont.render('排行榜',True,(255,0,0))
text_rect=textstart.get_rect()
text_rect.centerx=screen.get_rect().centerx
text_rect.centery=screen.get_rect().centery+120
screen.blit(textstart,text_rect)
arrayscore=read_text
startGame()
while True:
    for event in pygame.event.get():
        if event.type=pygame.QUIT:
            pygame.quit()
            exit()

     pygame.display.update()
