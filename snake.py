import pygame, random, math, sys
pygame.init()
W,H=1000,700; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("A.r CODEX • Neon Snake")
clock=pygame.time.Clock()
FONT=pygame.font.SysFont("arial",24,bold=True); BIG=pygame.font.SysFont("arial",54,bold=True)
BG=(9,12,24); PANEL=(18,23,42); WHITE=(235,242,255); CYAN=(70,230,210); PINK=(255,80,150); YELLOW=(255,210,70)

def reset():
    global snake,dirn,nextdir,food,score,gameover,paused,particles
    snake=[(10,10),(9,10),(8,10),(7,10)]; dirn=(1,0); nextdir=dirn
    food=(random.randrange(2,30),random.randrange(2,20)); score=0; gameover=False; paused=False; particles=[]
reset(); timer=0
def txt(s,pos,font=FONT,col=WHITE): screen.blit(font.render(s,True,col),pos)
def draw():
    screen.fill(BG)
    for x in range(0,W,40): pygame.draw.line(screen,(14,18,34),(x,0),(x,H),1)
    for y in range(0,H,40): pygame.draw.line(screen,(14,18,34),(0,y),(W,y),1)
    pygame.draw.rect(screen,PANEL,(70,75,860,560),border_radius=28)
    pygame.draw.rect(screen,(25,32,55),(110,120,780,500),border_radius=20)
    for i,(x,y) in enumerate(snake):
        c=CYAN if i==0 else (45,180,175)
        r=pygame.Rect(125+x*25,135+y*23,22,20); pygame.draw.rect(screen,c,r,border_radius=7)
    fx,fy=food; pygame.draw.circle(screen,PINK,(136+fx*25,145+fy*23),10)
    txt(f"SCORE  {score}",(90,25)); txt("R = restart   ESC = quit",(650,30),FONT,(150,160,185))
    if gameover:
        pygame.draw.rect(screen,(10,14,28),(270,245,460,190),border_radius=25)
        txt("GAME OVER",(370,275),BIG,PINK); txt(f"Score: {score}",(430,340)); txt("Press R to play again",(365,380),FONT,(180,190,215))
draw()
while True:
    dt=clock.tick(60)/1000
    for e in pygame.event.get():
        if e.type==pygame.QUIT: pygame.quit(); sys.exit()
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE: pygame.quit(); sys.exit()
            if e.key==pygame.K_r: reset()
            d={(pygame.K_UP):(0,-1),(pygame.K_DOWN):(0,1),(pygame.K_LEFT):(-1,0),(pygame.K_RIGHT):(1,0)}
            if e.key in d and d[e.key] != (-dirn[0],-dirn[1]): nextdir=d[e.key]
    if not gameover:
        timer+=dt
        if timer>.105:
            timer=0; dirn=nextdir; hx,hy=snake[0]; nx,ny=hx+dirn[0],hy+dirn[1]
            if nx<0 or nx>=31 or ny<0 or ny>=21 or (nx,ny) in snake[:-1]: gameover=True
            else:
                snake.insert(0,(nx,ny))
                if (nx,ny)==food:
                    score+=10
                    while food in snake: food=(random.randrange(2,30),random.randrange(2,20))
                else: snake.pop()
    draw(); pygame.display.flip()
