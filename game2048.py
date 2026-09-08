import pygame,sys,random
pygame.init();W,H=700,780;s=pygame.display.set_mode((W,H));pygame.display.set_caption("A.r CODEX • 2048")
F=pygame.font.SysFont("arial",28,bold=True);B=pygame.font.SysFont("arial",45,bold=True)
def reset():
 global a,score
 a=[[0]*4 for _ in range(4)];score=0;add()
def add():
 free=[(r,c) for r in range(4) for c in range(4) if a[r][c]==0]
 if free:r,c=random.choice(free);a[r][c]=4 if random.random()<.1 else 2
def move(row):
 z=[x for x in row if x];out=[];i=0
 while i<len(z):
  if i+1<len(z) and z[i]==z[i+1]:out.append(z[i]*2);globals()['score']+=z[i]*2;i+=2
  else:out.append(z[i]);i+=1
 return out+[0]*(4-len(out))
def go(d):
 global a
 old=[r[:] for r in a]
 if d=="L":a=[move(r) for r in a]
 if d=="R":a=[list(reversed(move(list(reversed(r))))) for r in a]
 if d=="U":a=[list(x) for x in zip(*[move(list(x)) for x in zip(*a)])]
 if d=="D":a=[list(x) for x in zip(*[list(reversed(move(list(reversed(x))))) for x in zip(*a)])]
 if a!=old:add()
reset()
while True:
 for e in pygame.event.get():
  if e.type==pygame.QUIT:pygame.quit();sys.exit()
  if e.type==pygame.KEYDOWN:
   if e.key==pygame.K_ESCAPE:pygame.quit();sys.exit()
   if e.key==pygame.K_r:reset()
   if e.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:go({pygame.K_LEFT:"L",pygame.K_RIGHT:"R",pygame.K_UP:"U",pygame.K_DOWN:"D"}[e.key])
 s.fill((10,12,20));pygame.draw.rect(s,(18,23,42),(50,35,600,700),border_radius=30)
 s.blit(B.render("2048",True,(240,245,255)),(80,65));s.blit(F.render("SCORE "+str(score),True,(160,175,195)),(430,82))
 for r in range(4):
  for c in range(4):
   q=pygame.Rect(80+c*130,160+r*130,115,115);pygame.draw.rect(s,(38,45,65) if not a[r][c] else (65,90,130),q,border_radius=14)
   if a[r][c]:v=str(a[r][c]);surf=B.render(v,True,(245,245,255));s.blit(surf,surf.get_rect(center=q.center))
 s.blit(F.render("Arrow keys • R restart • ESC exit",True,(150,160,180)),(115,705))
 pygame.display.flip();pygame.time.wait(16)
