import pygame, time
pygame.init()
screen=pygame.display.set_mode((500,300))
pygame.display.set_caption('Nguyen Hoang Thien')
run=True
k=1
diem=0
d_y=235
c_x=460
p1=False
p2=False
cl=pygame.time.Clock()
def show(k):
    if k==1:
        font=pygame.font.SysFont('arial',20)
        font_s=font.render('Score: {0}'.format(diem),True,(0,0,0))
        font_r=font_s.get_rect()
        font_r.midtop=(240,5)
        screen.blit(font_s,font_r)
    if k==2:
        font=pygame.font.SysFont('arial',30)
        font_s=font.render('Score: {0}'.format(diem),True,(255,0,0))
        font_r=font_s.get_rect()
        font_r.midtop=(15*12-5+25+45,150)
        screen.blit(font_s,font_r)
        font1=pygame.font.SysFont('arial',50)
        font_s1=font1.render('GAME OVER!',True,(255,0,0))
        font_r1=font_s1.get_rect()
        font_r1.midtop=(15*12-5+25+45,100)
        screen.blit(font_s1,font_r1)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE:
                if p2==False:
                    p1=True
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,285,500,5))
    screen.blit(pygame.image.load('dino.png'),(10,d_y))
    screen.blit(pygame.image.load('cactus.png'),(c_x,245))
    c_x-=5
    if c_x==-10: c_x=510
    if d_y==235: p2=False
    if d_y==135:
        p1=False
        p2=True
    if p1: d_y-=5
    if p2: d_y+=5
    if c_x>=10 and c_x<=40 and d_y+53>=245 and d_y+53<=288+53:
        k=2
    if c_x==5:
        diem+=1
    show(k)
    cl.tick(60)
    pygame.display.update()