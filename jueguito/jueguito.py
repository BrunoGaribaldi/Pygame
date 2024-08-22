import pygame,sys
pygame.init()

def circle_movement_without_player():
    global x_circle_speed
    global y_circle_speed
    global x_circle
    global y_circle
    if(x_circle > 790 or x_circle < 0):
        x_circle_speed *= -1

    if(y_circle > 490 or y_circle < 0):
        y_circle_speed *= -1


def circle_movement_with_player():
    global x_circle_speed
    global y_circle_speed
    global x_circle
    global y_circle 
    global x_player 
    global y_player 
    global width 
    global length 

    #rango del rectángulo
    rect_left = x_player 
    rect_right = x_player + width
    rect_top = y_player + length / 2
    rect_bottom = y_player - length / 2

    # punto mas cercano del rectangulo al centro de la pelota
    closest_x = max(rect_left, min(x_circle, rect_right))
    closest_y = max(rect_bottom, min(y_circle, rect_top))

    # formula 
    dx = x_circle - closest_x
    dy = y_circle - closest_y

    # comprobacion
    if dx * dx + dy * dy <= radious * radious:
        x_circle_speed *= -1
        y_circle_speed *= -1


            
BLACK  =  ( 0, 0, 0 )
WHITE  =  ( 255, 255, 255 )
RED    =  ( 255, 0, 0 )

x_circle = 400
y_circle = 200
radious = 10
x_circle_speed = 3
y_circle_speed = 3

x_player = 30
y_player = 0
width = 10
length = 30

size = (800,500)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()



pygame.mouse.set_visible(0)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mouse_pos = pygame.mouse.get_pos()
    y_player = mouse_pos[1]

    circle_movement_without_player()
    circle_movement_with_player()
    
    x_circle += x_circle_speed
    y_circle += y_circle_speed

    screen.fill(WHITE)

    pygame.draw.rect(screen,BLACK,(x_player,y_player,width,length))
    pygame.draw.circle(screen,RED,(x_circle,y_circle),radious)

    
    pygame.display.flip()
    clock.tick(60)