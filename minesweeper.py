import pygame,sys,random
pygame.init();W,H=900,700;s=pygame.display.set_mode((W,H));pygame.display.set_caption("A.r CODEX • Minesweeper")
F=pygame.font.SysFont("arial",22,bold=True);B=pygame.font.SysFont("arial",50,bold=True)
N=10; mines=set(random.sample(range(N*N),18));open_=set();flags=set()
def count(i):
 r,c=divmod(i,N);return sum((r+dr)*N+c+dc in mines for dr in (-1,0,1) for dc in (-1,0,1) if 0<=r+dr<N and 0<=c+dc<N)
while True:
 for e in pygame.event.get():
  if e.type==pygame.QUIT:pygame.quit();sys.exit()
  if e.type==pygame.KEYDOWN:
   if e.key==pygame.K_ESCAPE:pygame.quit();sys.exit()
   if e.key==pygame.K_r:mines=set(random.sample(range(N*N),18));open_=set();flags=set()
  if e.type==pygame.MOUSEBUTTONDOWN:
   x,y=e.pos
   if 190<x<710 and 100<y<620:
    c=(x-190)//52;r=(y-100)//52;i=r*N+c
    if e.button==3:flags.symmetric_difference_update({i})
    elif e.button==1 and i not in flags:open_.add(i)
 s.fill((8,11,22));pygame.draw.rect(s,(18,23,42),(80,35,740,630),border_radius=28)
 for i in range(N*N):
  r,c=divmod(i,N);q=pygame.Rect(190+c*52,100+r*52,48,48)
  pygame.draw.rect(s,(35,43,68) if i not in open_ else (20,80,85),q,border_radius=5)
  if i in flags:s.blit(F.render("F",True,(255,90,150)),(q.x+17,q.y+10))
  elif i in open_ and i in mines:s.blit(F.render("*",True,(255,90,150)),(q.x+17,q.y+10))
  elif i in open_:
   n=count(i)
   if n:s.blit(F.render(str(n),True,(240,245,255)),(q.x+17,q.y+10))
 s.blit(F.render("LEFT: open   RIGHT: flag   R: restart",True,(170,180,200)),(245,55))
 pygame.display.flip();pygame.time.wait(16)
