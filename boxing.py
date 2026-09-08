import pygame,sys,random
pygame.init();W,H=1000,700;s=pygame.display.set_mode((W,H));pygame.display.set_caption("A.r CODEX • Boxing")
clock=pygame.time.Clock();F=pygame.font.SysFont("arial",24,bold=True);B=pygame.font.SysFont("arial",55,bold=True)
hp1=hp2=100; t=0
while True:
 for e in pygame.event.get():
  if e.type==pygame.QUIT:pygame.quit();sys.exit()
  if e.type==pygame.KEYDOWN:
   if e.key==pygame.K_ESCAPE:pygame.quit();sys.exit()
   if e.key==pygame.K_r:hp1=hp2=100;t=0
   if e.key==pygame.K_f and hp2>0:hp2=max(0,hp2-random.randint(5,12))
   if e.key==pygame.K_l and hp1>0:hp1=max(0,hp1-random.randint(5,12))
 if hp1>0 and hp2>0:
  k=pygame.key.get_pressed()
  if k[pygame.K_j]:hp2=max(0,hp2-.08)
  if k[pygame.K_d]:hp1=max(0,hp1-.08)
 s.fill((12,10,18));pygame.draw.rect(s,(25,20,32),(45,45,910,600),border_radius=28)
 pygame.draw.rect(s,(120,35,45),(90,180,820,360),border_radius=20)
 pygame.draw.line(s,(235,235,235),(90,540),(910,540),8)
 # fighters
 pygame.draw.circle(s,(70,180,255),(310,330),55);pygame.draw.rect(s,(55,145,230),(275,385,70,125),border_radius=20)
 pygame.draw.circle(s,(255,90,130),(690,330),55);pygame.draw.rect(s,(230,65,105),(655,385,70,125),border_radius=20)
 s.blit(F.render("PLAYER 1  F punch",True,(90,200,255)),(90,90));s.blit(F.render("PLAYER 2  L punch",True,(255,100,140)),(650,90))
 pygame.draw.rect(s,(45,50,65),(100,145,350,20),border_radius=8);pygame.draw.rect(s,(70,200,255),(100,145,3.5*hp1,20),border_radius=8)
 pygame.draw.rect(s,(45,50,65),(550,145,350,20),border_radius=8);pygame.draw.rect(s,(255,80,130),(550,145,3.5*hp2,20),border_radius=8)
 if hp1<=0 or hp2<=0:
  msg="PLAYER 2 WINS" if hp1<=0 else "PLAYER 1 WINS";s.blit(B.render(msg,True,(245,245,255)),(335,575));s.blit(F.render("R to restart",True,(190,195,210)),(430,620))
 pygame.display.flip();clock.tick(60)
