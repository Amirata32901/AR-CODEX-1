import pygame,sys,random
pygame.init();W,H=900,650;s=pygame.display.set_mode((W,H));pygame.display.set_caption("A.r CODEX • Flappy")
clock=pygame.time.Clock();F=pygame.font.SysFont("arial",28,bold=True);B=pygame.font.SysFont("arial",60,bold=True)
def reset():
 global x,y,vy,pipes,score,over
 x,y,vy=180,300,0;pipes=[[650,random.randint(160,400)]];score=0;over=False
reset()
while True:
 for e in pygame.event.get():
  if e.type==pygame.QUIT:pygame.quit();sys.exit()
  if e.type==pygame.KEYDOWN:
   if e.key==pygame.K_ESCAPE:pygame.quit();sys.exit()
   if e.key in (pygame.K_SPACE,pygame.K_UP):vy=-9 if not over else -9; reset() if over else None
   if e.key==pygame.K_r:reset()
 if not over:
  vy+=.45;y+=vy
  for p in pipes:p[0]-=4
  if pipes[-1][0]<430:pipes.append([900,random.randint(160,400)])
  if pipes[0][0]<-90:pipes.pop(0);score+=1
  bird=pygame.Rect(x-18,y-14,36,28)
  for px,gap in pipes:
   if bird.colliderect((px,0,65,gap-75)) or bird.colliderect((px,gap+75,65,H)):over=True
  if y<0 or y>H:over=True
 s.fill((15,25,45));pygame.draw.rect(s,(20,35,60),(25,25,W-50,H-50),border_radius=25)
 for px,gap in pipes:
  pygame.draw.rect(s,(70,220,150),(px,45,65,gap-75),border_radius=10);pygame.draw.rect(s,(70,220,150),(px,gap+75,65,H-gap-100),border_radius=10)
 pygame.draw.circle(s,(255,210,70),(x,int(y)),20);pygame.draw.circle(s,(20,25,40),(x+7,int(y)-5),4)
 s.blit(F.render("SCORE "+str(score),True,(240,245,255)),(55,45))
 if over:s.blit(B.render("GAME OVER",True,(255,90,150)),(285,270));s.blit(F.render("SPACE / R to restart",True,(220,225,240)),(315,345))
 pygame.display.flip();clock.tick(60)
