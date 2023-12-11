import pygame

class Menu:
    def __init__(self):
        self.text_color_start = 'white'
        self.text_color_records = 'white'
        self.text_color_exit = 'white'

    def _click(position):
        if position == 1:
            return 1
        elif position == 2:
            return 2
        elif position == 3:
            return 3

    def menu_draw(self, screen, mouse_pos):
        screen.fill('black')
        if mouse_pos[0] >= 275 and mouse_pos[0] <= 509 and mouse_pos[1] >= 250 and mouse_pos[1] <= 289:
            self.text_color_start = 'red'
        else:
            self.text_color_start = 'white'
        if mouse_pos[0] >= 275 and mouse_pos[0] <= 509 and mouse_pos[1] >= 350 and mouse_pos[1] <= 389:
            self.text_color_records = 'red'
        else:
            self.text_color_records = 'white'
        if mouse_pos[0] >= 275 and mouse_pos[0] <= 509 and mouse_pos[1] >= 450 and mouse_pos[1] <= 489:
            self.text_color_exit = 'red'
        else:
            self.text_color_exit = 'white'
        font_game_name = pygame.font.Font('fonts/pixel.ttf', 60)
        font_autor = pygame.font.Font('fonts/pixel.ttf', 20)
        font = pygame.font.Font('fonts/pixel.ttf', 40)
        text_game_name = font_game_name.render('Dungeon', True, 'white')
        text_start = font.render('Играть', True, self.text_color_start)
        text_records = font.render('Рекорды', True, self.text_color_records)
        text_exit = font.render('Выход', True, self.text_color_exit)
        text_autor = font_autor.render('by Waxtep', True, 'white')
        screen.blit(text_game_name, (190, 50))
        screen.blit(text_start, (275, 250))
        screen.blit(text_records, (275, 350))
        screen.blit(text_exit, (275, 450))
        screen.blit(text_autor, (5, 575))
        pygame.display.update()
    
    def menu_event(self, mouse_pos):    
        if mouse_pos[0] >= 275 and mouse_pos[0] <= 509 and mouse_pos[1] >= 250 and mouse_pos[1] <= 289:
            return Menu._click(1)
        if mouse_pos[0] >= 275 and mouse_pos[0] <= 509 and mouse_pos[1] >= 350 and mouse_pos[1] <= 389:
            return Menu._click(2)
        if mouse_pos[0] >= 275 and mouse_pos[0] <= 509 and mouse_pos[1] >= 450 and mouse_pos[1] <= 489:
            return Menu._click(3)