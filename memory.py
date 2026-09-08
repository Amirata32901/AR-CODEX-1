import pygame,sys,random
pygame.init();W,H=900,700;s=pygame.display.set_mode((W,H));pygame.display.set_caption("A.r CODEX • Memory")
F=pygame.font.SysFont("arial",25,bold=True);B=pygame.font.SysFont("arial",55,bold=True)
vals=list(range(8))*2;random.shuffle(vals);cards=[None]*16;flipped=[];matched=set();moves=0
while True:
 for e in pygame.event.get():
  if e.type==pygame.QUIT:pygame.quit();sys.exit()
  if e.type==pygame.KEYDOWN:
   if e.key==pygame.K_ESCAPE:pygame.quit();sys.exit()
   if e.key==pygame.K_r:vals=list(range(8))*2;random.shuffle(vals);flipped=[];matched=set();moves=0
  if e.type==pygame.MOUSEBUTTONDOWN and e.button==1 and len(flipped)<2:
   x,y=e.pos
   if 160<x<740 and 130<y<610:
    c=(x-160)//145;r=(y-130)//120;i=r*4+c
    if i not in matched and i not in flipped:flipped.append(i)
 if len(flipped)==2:
  moves+=1
  if vals[flipped[0]]==vals[flipped[1]]:matched.update(flipped)
  else:pygame.time.delay(250)
  flipped=[]
 s.fill((8,11,22));pygame.draw.rect(s,(18,23,42),(45,35,810,630),border_radius=28)
 for i,v in enumerate(vals):
  r,c=divmod(i,4);rect=pygame.Rect(160+c*145,130+r*120,120,95)
  open_=i in matched or i in flipped
  pygame.draw.rect(s,(70,210,255) if open_ else (35,43,68),rect,border_radius=14)
  if open_:s.blit(B.render(str(v+1),True,(245,245,255)),(rect.centerx-17,rect.centery-28))
  else:pygame.draw.circle(s,(80,90,120),rect.center,8)
 s.blit(F.render(f"MOVES {moves}",True,(235,242,255)),(70,55));s.blit(F.render("R Restart • ESC Exit",True,(150,160,185)),(650,55))
 if len(matched)==16:s.blit(B.render("YOU WIN!",True,(80,230,180)),(350,80))
 pygame.display.flip();pygame.time.wait(16)
