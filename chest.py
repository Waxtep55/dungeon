import pygame, random

# список возможного содержимого сундука
loot = [100, 200, 500, 1000, 'potion']
class Chest:    
    def __init__(self):
        self.chance = random.randint(1, 100)
    
    # получить содержимое сундука
    def get_loot(self):
        if self.chance in range(1, 11):
            return loot[3]
        elif self.chance in range(11, 41):
            return loot[4]
        elif self.chance in range(41, 71):
            return loot[0]
        elif self.chance in range(71, 91):
            return loot[1]
        elif self.chance in range(91, 101):
            return loot[2]
    
    # нарисовать закрытый сундук
    def chest_draw(self, screen):
        chest_closed = pygame.image.load('img/elements/chest/chest_closed.png')
        font = pygame.font.Font('fonts/pixel.ttf', 40)
        text = font.render('Найден сундук!', True, 'white')
        screen.blit(text, (125, 100))
        screen.blit(chest_closed, (265, 175))
        pygame.display.update()
    
    # нарисовать открытый сундук
    def open_chest_draw(self, screen, loot):
        text1 = None
        chest_open = pygame.image.load('img/elements/chest/chest_open.png')
        font = pygame.font.Font('fonts/pixel.ttf', 40)
        screen.blit(chest_open, (265, 175))
        if loot == 'potion':
            text1 = font.render('Найдено  x1', True, 'white')
            potion = pygame.image.load('img/elements/health_potion.png')
            screen.blit(potion, (420, 98))
        else:
            text1 = font.render('Найдено  x' + str(loot), True, 'white')
            coin = pygame.image.load('img/elements/coin/coin_01.png')
            screen.blit(coin, (420, 98))
        screen.blit(text1, (125, 100))
        pygame.display.update()
