import pygame, random, time

# класс бой
class Fight:
    def __init__(self, player, monster):
        # сохраняем информацию об игроке и монстре
        self.player = {'health': player['health'], 'money': player['money'], 'potions': player['potions']}
        self.monster = {
            'name': monster['name'], 
            'health': monster['health'], 
            'damage': monster['damage'], 
            'sprites': monster['sprites']}
        # переменная ключа для спрайтов (анимация персонажа)
        self.img_key = 0
        # переменная для воспроизведения анимации
        self.animation = True
        # переменная для установления кол-ва фреймов
        self.clock = pygame.time.Clock()
    
    # зарисовать бой
    def fight_draw(self, screen, mouse_pos, move=1, attack=0, signal=0, miss=0):
        # чистка экрана
        screen.fill('black')
        # инициализируем переменные текста
        font = pygame.font.Font('fonts/pixel.ttf', 40)
        font_mini = pygame.font.Font('fonts/pixel.ttf', 30)
        monster_move_text = pygame.font.Font('fonts/pixel.ttf', 26).render('Ход противника', True, 'white')
        monster_name_text = font.render(self.monster['name'], True, 'white')
        monster_health_text = font_mini.render(str(self.monster['health']), True, 'white')
        # подгружаем изображения
        heart = pygame.image.load('img/elements/heart.png')
        coin = pygame.image.load('img/elements/coin/coin_01.png')
        potion = pygame.image.load('img/elements/health_potion.png')

        # выводим информацию на экран
        screen.blit(monster_name_text, (276, 44))
        screen.blit(heart, (391, 121))
        screen.blit(monster_health_text, (455, 132))

        # если ход игрока
        if move:
            color_1, color_2, color_3, color_4 = 'white', 'white', 'white', 'white'
            if miss:
                screen.blit(font_mini.render('Промах!', True, 'white'), (385, 231))
            else:
                screen.blit(font_mini.render('Ваш ход', True, 'white'), (385, 231))
            # если игрок атакует
            if attack:
                if mouse_pos[0] in range(419, 596) and mouse_pos[1] in range(423, 450):
                    color_1 = 'red'
                if mouse_pos[0] in range(419, 596) and mouse_pos[1] in range(463, 490):
                    color_2 = 'red'
                if mouse_pos[0] in range(419, 534) and mouse_pos[1] in range(503, 530):
                    color_3 = 'red'
                if mouse_pos[0] in range(419, 569) and mouse_pos[1] in range(543, 573):
                    color_4 = 'red'
                screen.blit(font_mini.render('Голова', True, color_1), (419, 423))
                screen.blit(font_mini.render('Корпус', True, color_2), (419, 463))
                screen.blit(font_mini.render('Ноги', True, color_3), (419, 503))
                screen.blit(font_mini.render('Назад', True, color_4), (419, 543))
            # если игрок выбирает действие
            else:
                if mouse_pos[0] in range(419, 685) and mouse_pos[1] in range(443, 471):
                    color_1 = 'red'
                if mouse_pos[0] in range(419, 775) and mouse_pos[1] in range(503, 530):
                    color_2 = 'red'
                screen.blit(font_mini.render('Атаковать', True, color_1), (419, 443))
                screen.blit(font_mini.render('Выпить зелье', True, color_2), (419, 503))
        # если ход противника
        else:
            self.clock.tick(10)
            if miss:
                screen.blit(font_mini.render('Промах!', True, 'white'), (385, 231))
            else:
                screen.blit(monster_move_text, (385, 231))
            if self.animation:
                if self.img_key != len(self.monster['sprites']) - 1:
                    self.img_key += 1
                else:
                    self.img_key = 0
                    self.animation = False
        # статичная информация
        screen.blit(self.monster['sprites'][self.img_key], (91, 121))
        pygame.draw.line(screen, 'white', [33, 403], [767, 403], 3)
        screen.blit(heart, (33, 423))
        screen.blit(font_mini.render(str(self.player['health']), True, 'white'), (95, 434))
        screen.blit(coin, (33, 483))
        screen.blit(font_mini.render(str(self.player['money']), True, 'white'), (95, 494))
        screen.blit(potion, (33, 543))
        color_potion = 'white'
        if signal:
            color_potion = 'red'
            screen.blit(font_mini.render(str(self.player['potions']), True, color_potion), (95, 554))
        screen.blit(font_mini.render(str(self.player['potions']), True, color_potion), (95, 554))

        pygame.display.update()
        if signal:
            time.sleep(0.1)

# рыцарь
class Knight:
    # задаем характеристики персонажу, подгружаем спрайты
    def __init__(self):
        self.name = 'Рыцарь'
        self.health = 60
        self.damage = 10
        self.weakness = 'legs'
        self.loot = {
            range(1, 41): 0,
            range(41, 91): 100,
            range(91, 101): 300
        }
        self.img = [
            pygame.image.load('img/elements/monsters/knight/knight1.png'),
            pygame.image.load('img/elements/monsters/knight/knight2.png'),
            pygame.image.load('img/elements/monsters/knight/knight3.png'),
            pygame.image.load('img/elements/monsters/knight/knight4.png'),
            pygame.image.load('img/elements/monsters/knight/knight5.png')
        ]
    
    # получить информацию о персонаже
    def get_info(self):
        return {'name': self.name, 'health': self.health, 'damage': self.damage, 'weakness': self.weakness, 'sprites': self.img}

    # получить лут
    def get_loot(self):
        chance = random.randint(1, 100)
        ranges = list(self.loot.keys())
        for _ in ranges:
            if chance in _:
                return self.loot[_]

    def _give_damage(self, damage):
        self.health -= damage

    # нанесение урона персонажу
    def give_damage(self, damage):
        # генерация шанса попадания
        chance = random.randint(1, 10)
        # если урон по слабому месту
        if damage == self.weakness:
            # шанс попадания - 30%
            if chance in range(1, 4):
                Knight._give_damage(self, 40)
                return 1
            else:
                return 0
        # если урон по любому другому месту
        else:
            # шанс попадания - 80%
            if chance in range(2, 11):
                Knight._give_damage(self, 20)
                return 1
            else:
                return 0

    # нанесение урона игроку
    def get_damage(self):
        # шанс попадания - 70%
        chance = random.randint(1, 10)
        if chance in range(4, 11):
            return self.damage
        else:
            return 0
    
    # возобновить информацию о монстре
    def update(self):
        self.health = 60

# темный рыцарь
class DarkKnight:
    # задаем характеристики персонажу, подгружаем спрайты
    def __init__(self):
        self.name = 'Тёмный рыцарь'
        self.health = 100
        self.damage = 20
        self.chance_damage = {
            'head': [70, 45],
            'body': [100, 30],
            'legs': [20, 70]
        }
        self.loot = {
            range(1, 31): 0,
            range(31, 61): 1,
            range(61, 101): 300
        }
        self.img = [
            pygame.image.load('img/elements/monsters/dark_knight/dark_knight1.png'),
            pygame.image.load('img/elements/monsters/dark_knight/dark_knight2.png'),
            pygame.image.load('img/elements/monsters/dark_knight/dark_knight3.png'),
            pygame.image.load('img/elements/monsters/dark_knight/dark_knight4.png')
        ]
    
    # получить информацию о персонаже
    def get_info(self):
        return {'name': self.name, 'health': self.health, 'damage': self.damage, 'sprites': self.img}
    
    # получить лут
    def get_loot(self):
        chance = random.randint(1, 100)
        ranges = list(self.loot.keys())
        for _ in ranges:
            if chance in _:
                return self.loot[_]

    def _give_damage(self, damage):
        self.health -= damage

    # нанесение урона персонажу
    def give_damage(self, damage):
        # генерация шанса попадания
        chance = random.randint(1, 100)
        if chance in range(100 - self.chance_damage[damage][0], 100):
            DarkKnight._give_damage(self, self.chance_damage[damage][1])
            return 1
        else:
            return 0
        
    # нанесение урона игроку
    def get_damage(self):
        # шанс попадания - 60%
        chance = random.randint(1, 10)
        if chance in range(5, 11):
            return self.damage
        else:
            return 0
    
    # возобновить информацию о монстре
    def update(self):
        self.health = 100

# модный рыцарь
class FashionKnight:
    # задаем характеристики персонажу, подгружаем спрайты
    def __init__(self):
        self.name = 'Модный рыцарь'
        self.health = 75
        self.damage = 15
        self.chance_damage = {
            'head': [20, 75],
            'body': [90, 20],
            'legs': [60, 30]
        }
        self.loot = {
            range(1, 41): 1,
            range(41, 81): 600,
            range(81, 101): 1000
        }
        self.img = [
            pygame.image.load('img/elements/monsters/fashion_knight/fashion_knight1.png'),
            pygame.image.load('img/elements/monsters/fashion_knight/fashion_knight2.png'),
            pygame.image.load('img/elements/monsters/fashion_knight/fashion_knight3.png'),
            pygame.image.load('img/elements/monsters/fashion_knight/fashion_knight4.png'),
            pygame.image.load('img/elements/monsters/fashion_knight/fashion_knight5.png'),
            pygame.image.load('img/elements/monsters/fashion_knight/fashion_knight6.png'),
            pygame.image.load('img/elements/monsters/fashion_knight/fashion_knight7.png'),
            pygame.image.load('img/elements/monsters/fashion_knight/fashion_knight8.png'),
        ]
    
    # получить информацию о персонаже
    def get_info(self):
        return {'name': self.name, 'health': self.health, 'damage': self.damage, 'sprites': self.img}

    # получить лут
    def get_loot(self):
        chance = random.randint(1, 100)
        ranges = list(self.loot.keys())
        for _ in ranges:
            if chance in _:
                return self.loot[_]
    
    def _give_damage(self, damage):
        self.health -= damage

    # нанесение урона персонажу
    def give_damage(self, damage):
        # генерация шанса попадания
        chance = random.randint(1, 100)
        if chance in range(100 - self.chance_damage[damage][0], 100):
            FashionKnight._give_damage(self, self.chance_damage[damage][1])
            return 1
        else:
            return 0
        
    # нанесение урона игроку
    def get_damage(self):
        # шанс попадания - 80%
        chance = random.randint(1, 10)
        if chance in range(3, 11):
            return self.damage
        else:
            return 0
    
    # возобновить информацию о монстре
    def update(self):
        self.health = 75

# вампир
class Vampire:
    # задаем характеристики персонажу, подгружаем спрайты
    def __init__(self):
        self.name = 'Вампир'
        self.health = 120
        self.damage = 15
        self.chance_damage = {
            'head': [30, 100],
            'body': [75, 30],
            'legs': [50, 50]
        }
        self.loot = {
            range(1, 21): 0,
            range(21, 51): 1,
            range(51, 91): 2,
            range(91, 101): 800
        }
        self.img = [
            pygame.image.load('img/elements/monsters/vampire/vampire1.png'),
            pygame.image.load('img/elements/monsters/vampire/vampire2.png'),
            pygame.image.load('img/elements/monsters/vampire/vampire3.png'),
            pygame.image.load('img/elements/monsters/vampire/vampire4.png')
        ]
    
    # получить информацию о персонаже
    def get_info(self):
        return {'name': self.name, 'health': self.health, 'damage': self.damage, 'sprites': self.img}

    # получить лут
    def get_loot(self):
        chance = random.randint(1, 100)
        ranges = list(self.loot.keys())
        for _ in ranges:
            if chance in _:
                return self.loot[_]
    
    def _give_damage(self, damage):
        self.health -= damage

    # нанесение урона персонажу
    def give_damage(self, damage):
        # генерация шанса попадания
        chance = random.randint(1, 100)
        if chance in range(100 - self.chance_damage[damage][0], 100):
            Vampire._give_damage(self, self.chance_damage[damage][1])
            return 1
        else:
            return 0
        
    # нанесение урона игроку
    def get_damage(self):
        # шанс попадания - 100%
        return self.damage

    
    # возобновить информацию о монстре
    def update(self):
        self.health = 120

# гоблин
class Goblin:
    # задаем характеристики персонажу, подгружаем спрайты
    def __init__(self):
        self.name = 'Гоблин'
        self.health = 50
        self.damage = 50
        self.chance_damage = {
            'head': [20, 50],
            'body': [50, 25],
            'legs': [20, 50]
        }
        self.loot = {
            range(1, 51): 0,
            range(51, 101): 400
        }
        self.img = [
            pygame.image.load('img/elements/monsters/goblin/goblin1.png'),
            pygame.image.load('img/elements/monsters/goblin/goblin2.png'),
            pygame.image.load('img/elements/monsters/goblin/goblin3.png'),
            pygame.image.load('img/elements/monsters/goblin/goblin4.png')
        ]
    
    # получить информацию о персонаже
    def get_info(self):
        return {'name': self.name, 'health': self.health, 'damage': self.damage, 'sprites': self.img}
    
    # получить лут
    def get_loot(self):
        chance = random.randint(1, 100)
        ranges = list(self.loot.keys())
        for _ in ranges:
            if chance in _:
                return self.loot[_]

    def _give_damage(self, damage):
        self.health -= damage

    # нанесение урона персонажу
    def give_damage(self, damage):
        # генерация шанса попадания
        chance = random.randint(1, 100)
        if chance in range(100 - self.chance_damage[damage][0], 100):
            Goblin._give_damage(self, self.chance_damage[damage][1])
            return 1
        else:
            return 0
        
    # нанесение урона игроку
    def get_damage(self):
        # шанс попадания - 20%
        chance = random.randint(1, 10)
        if chance in range(9, 11):
            return self.damage
        else:
            return 0
    
    # возобновить информацию о монстре
    def update(self):
        self.health = 50

# слизень
class Slime:
    # задаем характеристики персонажу, подгружаем спрайты
    def __init__(self):
        self.name = 'Слизень'
        self.health = 40
        self.damage = 10
        self.chance_damage = {
            'head': [50, 25],
            'body': [100, 10],
            'legs': [0, 0]
        }
        self.loot = {
            range(1, 41): 0,
            range(41, 55): 1,
            range(55, 101): 200
        }
        
        self.img = [
            pygame.image.load('img/elements/monsters/slime/slime1.png'),
            pygame.image.load('img/elements/monsters/slime/slime2.png'),
            pygame.image.load('img/elements/monsters/slime/slime3.png'),
            pygame.image.load('img/elements/monsters/slime/slime4.png'),
            pygame.image.load('img/elements/monsters/slime/slime5.png'),
            pygame.image.load('img/elements/monsters/slime/slime6.png'),
            pygame.image.load('img/elements/monsters/slime/slime7.png'),
            pygame.image.load('img/elements/monsters/slime/slime8.png'),
        ]
    
    # получить информацию о персонаже
    def get_info(self):
        return {'name': self.name, 'health': self.health, 'damage': self.damage, 'sprites': self.img}
    
    # получить лут
    def get_loot(self):
        chance = random.randint(1, 100)
        ranges = list(self.loot.keys())
        for _ in ranges:
            if chance in _:
                return self.loot[_]
                
    def _give_damage(self, damage):
        self.health -= damage

    # нанесение урона персонажу
    def give_damage(self, damage):
        # генерация шанса попадания
        chance = random.randint(1, 100)
        if chance in range(100 - self.chance_damage[damage][0], 100):
            Slime._give_damage(self, self.chance_damage[damage][1])
            return 1
        else:
            return 0
        
    # нанесение урона игроку
    def get_damage(self):
        # шанс попадания - 80%
        chance = random.randint(1, 10)
        if chance in range(3, 11):
            return self.damage
        else:
            return 0
    
    # возобновить информацию о монстре
    def update(self):
        self.health = 40