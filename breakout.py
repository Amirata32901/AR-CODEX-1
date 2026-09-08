import pygame,sys,random
pygame.init();W,H=1000,700;s=pygame.display.set_mode((W,H));pygame.display.set_caption("A.r CODEX • Breakout")
clock=pygame.time.Clock();F=pygame.font.SysFont("arial",25,bold=True);B=pygame.font.SysFont("arial",55,bold=True)
def reset():
 global px,bx,by,vx,vy,bricks,score,lives,over
 px=425;bx,by=500,560;vx,vy=5,-5;score=0;lives=3;over=False
 bricks=[pygame.Rect(90+c*92,100+r*32,80,22) for r in range(6) for c in range(9)]
reset()
while True:
 for e in pygame.event.get():
  if e.type==pygame.QUIT:pygame.quit();sys.exit()
  if e.type==pygame.KEYDOWN:
   if e.key==pygame.K_ESCAPE:pygame.quit();sys.exit()
   if e.key==pygame.K_r:reset()
 k=pygame.key.get_pressed();px=max(50,min(W-170,px+(-9 if k[pygame.K_LEFT] else 9 if k[pygame.K_RIGHT] else 0)))
 if not over:
  bx+=vx;by+=vy
  if bx<50 or bx>950:vx*=-1
  if by<55:vy*=-1
  ball=pygame.Rect(bx-8,by-8,16,16);pad=pygame.Rect(px,620,150,18)
  if ball.colliderect(pad) and vy>0:vy=-abs(vy)
  for b in bricks[:]:
   if ball.colliderect(b):bricks.remove(b);vy*=-1;score+=10;break
  if by>720:lives-=1;bx,by=500,560;vx=random.choice([-5,5]);vy=-5;over=lives<=0
 s.fill((8,11,22));pygame.draw.rect(s,(18,23,42),(35,35,930,610),border_radius=28)
 for i,b in enumerate(bricks):pygame.draw.rect(s,(70+((i*17)%130),120,240),b,border_radius=6)
 pygame.draw.rect(s,(80,210,255),(px,620,150,18),border_radius=9);pygame.draw.circle(s,(245,245,255),(bx,by),9)
 s.blit(F.render(f"SCORE {score}     LIVES {lives}",True,(235,242,255)),(65,50))
 if over:s.blit(B.render("GAME OVER",True,(255,90,150)),(360,300));s.blit(F.render("R to restart",True,(220,225,240)),(430,365))
 pygame.display.flip();clock.tick(60)
