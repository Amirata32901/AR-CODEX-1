import pygame,sys,random,math
pygame.init();W,H=1000,700;s=pygame.display.set_mode((W,H));pygame.display.set_caption("A.r CODEX • Space Shooter")
clock=pygame.time.Clock();F=pygame.font.SysFont("arial",24,bold=True);B=pygame.font.SysFont("arial",55,bold=True)
def reset():
 global ship,bullets,enemies,score,lives,over,stars
 ship=pygame.Rect(475,600,50,35);bullets=[];enemies=[];score=0;lives=3;over=False;stars=[(random.randrange(W),random.randrange(H),random.randrange(1,4)) for _ in range(100)]
reset();spawn=0
while True:
 for e in pygame.event.get():
  if e.type==pygame.QUIT:pygame.quit();sys.exit()
  if e.type==pygame.KEYDOWN:
   if e.key==pygame.K_ESCAPE:pygame.quit();sys.exit()
   if e.key==pygame.K_r:reset()
   if e.key==pygame.K_SPACE and not over:bullets.append(pygame.Rect(ship.centerx-3,ship.y-15,6,18))
 if not over:
  k=pygame.key.get_pressed();ship.x+=(-8 if k[pygame.K_LEFT] else 8 if k[pygame.K_RIGHT] else 0);ship.x=max(40,min(W-90,ship.x))
  for b in bullets:b.y-=12
  bullets[:]=[b for b in bullets if b.y>-20]
  spawn+=1
  if spawn>30:enemies.append(pygame.Rect(random.randrange(50,930),-30,42,30));spawn=0
  for en in enemies:en.y+=3
  for b in bullets[:]:
   for en in enemies[:]:
    if b.colliderect(en):bullets.remove(b);enemies.remove(en);score+=10;break
  for en in enemies[:]:
   if en.colliderect(ship) or en.y>700:enemies.remove(en);lives-=1
  if lives<=0:over=True
 s.fill((4,7,18))
 for x,y,z in stars:pygame.draw.circle(s,(80+z*40,90+z*35,130+z*30),(x,y),z)
 pygame.draw.rect(s,(15,20,38),(30,30,940,620),border_radius=28)
 pygame.draw.polygon(s,(70,210,255),[(ship.centerx,ship.y-12),(ship.x,ship.bottom),(ship.right,ship.bottom)])
 for b in bullets:pygame.draw.rect(s,(255,220,80),b,border_radius=3)
 for en in enemies:pygame.draw.polygon(s,(255,80,150),[(en.centerx,en.bottom),(en.x,en.y),(en.right,en.y)])
 s.blit(F.render(f"SCORE {score}   LIVES {lives}",True,(235,242,255)),(55,50))
 if over:s.blit(B.render("MISSION FAILED",True,(255,90,150)),(300,300));s.blit(F.render("R to restart",True,(220,225,240)),(440,370))
 pygame.display.flip();clock.tick(60)
