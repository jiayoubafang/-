#引入pygame模块 用cmd pip install pygame
import pygame;
#pygame 中的常量
from pygame.locals impport*
#游戏主循环结束后 游戏画面
screen.blit(game_over,(0,0))
font=pygame.font.Font(None,48)
text=font.render('Score:'+str(score),Trut,(255,0,0))
text_rect=text.get_rect()
text_rect.centerx=screen.get_rect().centerx
text_rect.centery=screen.get_rect().centery+24
screen.blit(text,text_rect)
#重新开始按钮
xtfont=pygame.font.SysFont('SimHei',30)
textstart=xtfont.render('排行榜',True,(255,0,0))
text_rect=textstart.get_rect()
text_rect.centerx=screen.get_rect().centerx
text_rect.centery=screen.get_rect().centery+180
screen.blit(textstart,text_rect)
#排行榜
textstart=xtfont.render('重新开始',True,(255,0,0))
text_rect=textstart.get_rect()
text_rect.centerx=screen.get_rect().centerx
text_rect.centery=screen.get_rect().centery+120
screen.blit(textstart,text_rect)
startGame()
while True:
    for event in pygame.event.get():
        if event.type=pygame.QUIT:
            pygame.quit()
            exit()

     pygame.display.update()
