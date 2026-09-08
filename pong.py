import pygame,sys,random
pygame.init(); W,H=1000,700; s=pygame.display.set_mode((W,H)); pygame.display.set_caption("A.r CODEX • Neon Pong")
clock=pygame.time.Clock(); F=pygame.font.SysFont("arial",26,bold=True); B=pygame.font.SysFont("arial",58,bold=True)
p1=H//2-60;p2=p1; bx,by=W//2,H//2; vx,vy=6,random.choice([-4,4]); sc1=sc2=0
while True:
 for e in pygame.event.get():
  if e.type==pygame.QUIT: pygame.quit();sys.exit()
  if e.type==pygame.KEYDOWN:
   if e.key==pygame.K_ESCAPE: pygame.quit();sys.exit()
   if e.key==pygame.K_r: p1=p2=H//2-60;sc1=sc2=0
 keys=pygame.key.get_pressed()
 if keys[pygame.K_w]:p1-=8
 if keys[pygame.K_s]:p1+=8
 if keys[pygame.K_UP]:p2-=8
 if keys[pygame.K_DOWN]:p2+=8
 p1=max(70,min(H-190,p1));p2=max(70,min(H-190,p2))
 # AI-ish paddle follows if no keyboard? right is still keyboard
 bx+=vx;by+=vy
 if by<70 or by>H-70:vy*=-1
 b=pygame.Rect(bx-10,by-10,20,20)
 if b.colliderect((60,p1,18,120)) and vx<0: vx=abs(vx)*1.03
 if b.colliderect((W-78,p2,18,120)) and vx>0: vx=-abs(vx)*1.03
 if bx<0:sc2+=1;bx,by=W//2,H//2;vx=6
 if bx>W:sc1+=1;bx,by=W//2,H//2;vx=-6
 s.fill((7,10,20));pygame.draw.rect(s,(18,23,42),(35,35,W-70,H-70),border_radius=25)
 for y in range(80,H-80,32):pygame.draw.rect(s,(55,65,90),(W//2-3,y,6,18),border_radius=3)
 pygame.draw.rect(s,(70,210,255),(60,p1,18,120),border_radius=9);pygame.draw.rect(s,(255,85,155),(W-78,p2,18,120),border_radius=9)
 pygame.draw.circle(s,(235,245,255),(bx,by),12)
 s.blit(B.render(str(sc1),True,(70,210,255)),(400,55));s.blit(B.render(str(sc2),True,(255,85,155)),(555,55))
 s.blit(F.render("W/S       UP/DOWN       R Restart       ESC",True,(150,160,180)),(275,640))
 pygame.display.flip();clock.tick(60)
