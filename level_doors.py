import pygame, random

class Door:
    def __init__(self):
        self.door_left_anim_key = 0
        self.door_right_anim_key = 0
        self.clock = pygame.time.Clock()
        # рандомно определяем, за какой дверью сундук, а за какой - монстр
        self.lucky_door = random.randint(0, 1)

    # открываем дверь
    def open_door(self, mouse_pos):
        # если открыта правая дверь
        if mouse_pos[0] >= 500 and mouse_pos[0] <= 633 and mouse_pos[1] >= 250 and mouse_pos[1] <= 415:
            if self.lucky_door == 1:
                return 'chest'
            else:
                return 'monster'
        # если открыта левая дверь
        elif mouse_pos[0] >= 150 and mouse_pos[0] <= 283 and mouse_pos[1] >= 250 and mouse_pos[1] <= 415:
            if self.lucky_door == 0:
                return 'chest'
            else:
                return 'monster'
        else:
            return 0
    
    # рисуем дверь
    def door_draw(self, screen, mouse_pos):
        door = [
            pygame.image.load('img/elements/doors/doors1.png'),
            pygame.image.load('img/elements/doors/doors2.png'),
            pygame.image.load('img/elements/doors/doors3.png'),
            pygame.image.load('img/elements/doors/doors4.png'),
            pygame.image.load('img/elements/doors/doors5.png'),
            pygame.image.load('img/elements/doors/doors6.png')
        ]
        
        font = pygame.font.Font('fonts/pixel.ttf', 40)
        text = font.render('Выбери дверь', True, 'white')
        # выводим на экран двери и надпись
        screen.fill('black')
        screen.blit(text, (150, 100))
        screen.blit(door[self.door_left_anim_key], (150, 250))
        screen.blit(door[self.door_right_anim_key], (500, 250))

        # обновляем экран
        pygame.display.update()
        # анимация дверей
        if mouse_pos[0] >= 500 and mouse_pos[0] <= 633 and mouse_pos[1] >= 250 and mouse_pos[1] <= 415:
            if self.door_right_anim_key != 5:
                self.door_right_anim_key += 1
        else:
            if self.door_right_anim_key != 0:
                self.door_right_anim_key -= 1
        if mouse_pos[0] >= 150 and mouse_pos[0] <= 283 and mouse_pos[1] >= 250 and mouse_pos[1] <= 415:
            if self.door_left_anim_key != 5:
                self.door_left_anim_key += 1
        else:
            if self.door_left_anim_key != 0:
                self.door_left_anim_key -= 1
        # указываем количество фреймов за секунду
        self.clock.tick(15)