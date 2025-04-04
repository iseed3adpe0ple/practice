import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_x:
                    points = []
            
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_z:
                    mode = 'square'
                elif event.key == pygame.K_t:
                    mode = 'right_triangle'
                elif event.key == pygame.K_e:
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_d:
                    mode = 'rhombus'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append((position, mode))
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        for i in range(len(points)):
            pos, shape = points[i]
            if shape == 'square':
                drawSquare(screen, pos, radius)
            elif shape == 'right_triangle':
                drawRightTriangle(screen, pos, radius)
            elif shape == 'equilateral_triangle':
                drawEquilateralTriangle(screen, pos, radius)
            elif shape == 'rhombus':
                drawRhombus(screen, pos, radius)
            else:
                drawLineBetween(screen, i, pos, radius, shape)
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, position, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    else:
        color = (255, 255, 255)
    
    pygame.draw.circle(screen, color, position, width)

def drawSquare(screen, position, size):
    pygame.draw.rect(screen, (255, 255, 255), (position[0] - size // 2, position[1] - size // 2, size, size))

def drawRightTriangle(screen, position, size):
    points = [position, (position[0] + size, position[1]), (position[0], position[1] + size)]
    pygame.draw.polygon(screen, (255, 255, 255), points)

def drawEquilateralTriangle(screen, position, size):
    h = (3 ** 0.5 / 2) * size
    points = [
        (position[0], position[1] - h // 2),
        (position[0] - size // 2, position[1] + h // 2),
        (position[0] + size // 2, position[1] + h // 2)
    ]
    pygame.draw.polygon(screen, (255, 255, 255), points)

def drawRhombus(screen, position, size):
    points = [
        (position[0], position[1] - size // 2),
        (position[0] + size // 2, position[1]),
        (position[0], position[1] + size // 2),
        (position[0] - size // 2, position[1])
    ]
    pygame.draw.polygon(screen, (255, 255, 255), points)

main()
