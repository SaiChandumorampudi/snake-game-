import pygame
import time
import random

pygame.init()

white=(255,55,255)
yellow=(255,255,102)
red=(213,50,80)
black=(0,0,0)
green=(0,255,0)
blue=(50,153,213)

dis_height=400
dis_width=600
dis=pygame.display.set_mode((dis_height,dis_width))
pygame.display.set_caption("python_snake")
clock=pygame.time.Clock()
snake_block=10
snake_speed=10
font_style=pygame.font.SysFont("italic",25)
score_font=pygame.font.SysFont("impact",20)
def your_score(score):
    value=score_font.render("Score:"+str(score),True,black)
    dis.blit(value,[0,0])
def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[1],x[0],snake_block,snake_block])
def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/6,dis_height/3])

def gameLoop():
    game_over=False
    game_close=False
    x1=dis_width/2
    y1=dis_height/2
    x1_change=0
    y1_change=0
    snake_list=[]
    Length_of_snake=1
    foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
    while not game_over:
        while game_close==True:
            dis.fill(blue)
            lost="your lost press C to play again or Q to quit"
            message(lost,red)
            your_score(Length_of_snake-1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_DOWN:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_LEFT:
                    y1_change=-snake_block
                    x1_change=0
                elif event.key==pygame.K_RIGHT:
                    y1_change=snake_block
                    x1_change=0 
        if x1>=dis_width or x1 < 0 or y1 >=dis_height or y1 < 0:
            game_close=True
        x1+=x1_change
        y1+=y1_change
        dis.fill(blue)
        pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block]) 
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list)>Length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_Head:
                game_close=True
        our_snake(snake_block,snake_list)
        your_score(Length_of_snake -1)
        pygame.display.update()
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0 
            foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
            Length_of_snake +=1
        clock.tick(snake_speed)
    pygame.quit
    quit()
gameLoop()                    
 