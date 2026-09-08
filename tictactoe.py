import pygame, sys, random
pygame.init()
W,H=1000,700; screen=pygame.display.set_mode((W,H)); pygame.display.set_caption("A.r CODEX • Tic Tac Toe")
clock=pygame.time.Clock(); F=pygame.font.SysFont("arial",25,bold=True); B=pygame.font.SysFont("arial",62,bold=True)
BG=(8,11,22); PANEL=(18,23,42); GRID=(55,68,100); X=(80,190,255); O=(255,90,155); WHITE=(240,245,255)
board=[[""]*3 for _ in range(3)]; mode="AI"; turn="X"; winner=None; score=[0,0]
def reset(): 
    global board,turn,winner; board=[[""]*3 for _ in range(3)]; turn="X"; winner=None
def lines():
    z=board
    return [z[0],z[1],z[2],[z[i][j] for i in range(3) for j in [i]], [z[i][2-i] for i in range(3)]]+[[z[i][j] for i in range(3)] for j in range(3)]
def result():
    for a in lines():
        if a[0] and a.count(a[0])==3:return a[0]
    if all(all(r) for r in board):return "DRAW"
    return None
def ai():
    free=[(r,c) for r in range(3) for c in range(3) if not board[r][c]]
    if not free:return
    # strategic priority
    for p in ["O","X"]:
        for r,c in free:
            board[r][c]=p
            if result()==p: board[r][c]=""; return (r,c)
            board[r][c]=""
    return random.choice(free)
def draw():
    screen.fill(BG); pygame.draw.rect(screen,PANEL,(40,35,920,630),border_radius=30)
    t=F.render("TIC TAC TOE",True,WHITE); screen.blit(t,(70,60))
    pygame.draw.rect(screen,(25,31,53),(270,120,460,460),border_radius=24)
    for i in range(1,3):
        pygame.draw.line(screen,GRID,(270+i*153,145),(270+i*153,555),7)
        pygame.draw.line(screen,GRID,(295,120+i*153),(705,120+i*153),7)
    for r in range(3):
        for c in range(3):
            cx,cy=346+c*153,197+r*153
            if board[r][c]=="X":
                pygame.draw.line(screen,X,(cx-45,cy-45),(cx+45,cy+45),12)
                pygame.draw.line(screen,X,(cx+45,cy-45),(cx-45,cy+45),12)
            elif board[r][c]=="O": pygame.draw.circle(screen,O,(cx,cy),45,11)
    if winner:
        msg="DRAW" if winner=="DRAW" else winner+" WINS!"
        pygame.draw.rect(screen,(12,17,32),(300,585,400,55),border_radius=18)
        screen.blit(F.render(msg,True,O if winner=="O" else X),(430,595))
    screen.blit(F.render("R Restart   M Toggle AI/2P   ESC Exit",True,(150,160,185)),(270,620))
while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: pygame.quit();sys.exit()
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE: pygame.quit();sys.exit()
            if e.key==pygame.K_r: reset()
            if e.key==pygame.K_m: mode="2P" if mode=="AI" else "AI"; reset()
        if e.type==pygame.MOUSEBUTTONDOWN and e.button==1 and not winner:
            x,y=e.pos
            if 270<x<730 and 120<y<580:
                c=(x-270)//153; r=(y-120)//153
                if not board[r][c]:
                    board[r][c]=turn; winner=result()
                    if winner: score[0 if winner=="X" else 1]+=1
                    else:
                        turn="O" if turn=="X" else "X"
                        if mode=="AI" and turn=="O":
                            p=ai()
                            if p: board[p[0]][p[1]]="O"; winner=result()
                            if not winner: turn="X"
    draw(); pygame.display.flip(); clock.tick(60)
