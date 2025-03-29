import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

_songs = ['sound1.mp3', 'sound2.mp3', 'sound3.mp3']
i = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if i < 2:
                    i += 1
                    print(i)
            if event.key == pygame.K_s:
                if i > 0:
                    i -= 1
                    print(i)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        pygame.mixer.music.load(_songs[i])
        pygame.mixer.music.play(0)
    if pressed[pygame.K_t]:
        pygame.mixer.music.stop()

    pygame.display.flip()
