import pygame

def draw(screen, info, set_record=False, player_name=''):
    screen.fill('black')
    font1 = pygame.font.Font('fonts/pixel.ttf', 60)
    font2 = pygame.font.Font('fonts/pixel.ttf', 40)
    if not set_record:
        text1 = font1.render('Game over', True, 'white')
        text2 = font2.render('Счёт: ' + str(info['money']), True, 'white')
        screen.blit(text1, (156, 172))
        screen.blit(text2, (265, 369))
    else:
        text1 = font2.render('Введите своё имя', True, 'white')
        text2 = font1.render(player_name, True, 'white')
        screen.blit(text1, (93, 172))
        screen.blit(text2, (293, 369))
    pygame.display.update()