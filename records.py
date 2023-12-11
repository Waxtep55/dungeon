import pygame

def records_draw(screen, mouse_pos, filename):
    file = open(filename, 'r')
    screen.fill('black')
    main_font = pygame.font.Font('fonts/pixel.ttf', 60)
    font = pygame.font.Font('fonts/pixel.ttf', 40)
    main_text = main_font.render('Рекорды', True, 'white')
    color = 'white'
    if mouse_pos[0] in range(270, 470) and mouse_pos[1] in range(527, 568):
        color = 'red'
    text_exit = font.render('Назад', True, color)
    screen.blit(main_text, (185, 40))
    screen.blit(text_exit, (270, 527))
    text = []
    lines = file.readlines()
    for line in range(0, len(lines) - 1):
        a = lines[line].replace('\n', '')
        if a == '':
            continue
        text.append(str(line + 1) + ' ' + a)
    file.close()
    y = 140
    cycle = 0
    for line in text:
        if cycle == 8:
            break
        screen.blit(font.render(line, True, 'white'), (185, y))
        y += 45
        cycle += 1
    pygame.display.update()