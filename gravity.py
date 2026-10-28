import pygame , math

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
x ,y  = 400,0
new_t=0
t=0 
radius = 70
sx = abs((x+radius)-(x-radius))/2
sy = abs((y+radius)-(y-radius))/2
v=0
runnig = True
while runnig:
    tc = (clock.tick(60))
    dt = tc/1000
    t+=dt
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False    

    a =9.8
    v =v+a*dt
    y =y+v*dt
 
    if y<0 :  y = 0
    if y>600-sx : y=600-sx
    
    color = (
        int(200),
        int(0),
        int(0)
    )
    screen.fill((20,20,40))
    pygame.draw.circle(screen,color,(int(x),int(y)),int(radius))
    pygame.display.flip()
    new_t += tc
    if(new_t>=1000):
        new_t-=1000 
        print(y)
    
    
    
pygame.quit()