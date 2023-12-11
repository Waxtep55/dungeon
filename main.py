import pygame, menu, level_doors, player, chest, monsters, game_over, records, sort_records, win
import time, random

clock = pygame.time.Clock()

# инициализируем игру
# с этого момента начинается разработка игры
pygame.init()
# создание экрана (ф-я принимает кортеж с заданными шириной и высотой экрана)
screen = pygame.display.set_mode((800, 600)) #, flags=pygame.NOFRAME
# подпись на рамке
pygame.display.set_caption('Dungeon by Waxtep')
# подгрузка изображения
icon = pygame.image.load('img/icon.png')
# добавляем иконку в дисплей
pygame.display.set_icon(icon)
# подгрузка аудиофайла
bg_sound = pygame.mixer.Sound('sound/menu.mp3')
fight_sound = pygame.mixer.Sound('sound/fight.mp3')
# запуск аудиофайла
bg_sound.play()

# инициализируем класс меню
start = menu.Menu()
# инициализируем класс уровня с дверьми
door = level_doors.Door()
# переменная текущего окна
window = 'menu'
# переменная класса игрок
my_player = player.Player()
# имя игрока
player_name = ''
# кол-во введенных игроком символов (для установления рекорда)
count_symbols = 0
# ход игрока
move = 1
# атака игрока
attack = 0
# сигнал об отсутсвии зелий
signal = 0
# сигнал о промахе
miss = 0
# переменная класса сундук
my_chest = chest.Chest()
# инициализируем монстров
knight = monsters.Knight()
dark_knight = monsters.DarkKnight()
fashion_knight = monsters.FashionKnight()
vampire = monsters.Vampire()
goblin = monsters.Goblin()
slime = monsters.Slime()
# переменная класса битвы
fight = monsters.Fight(my_player.get_info(), knight.get_info())
# список монстров
monster = [knight, dark_knight, fashion_knight, vampire, goblin, slime]
# переменная текущего монстра
rand_monster = None
# переменная для проигрывания анимации врага
cycle = True
# переменная упавшего лута с монстра
loot = 0

# цикл происходящего на экране
running = True
while running:
    # поизиция мыши
    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)
    # зарисовка уровней
    if window == 'menu':
        start.menu_draw(screen, mouse_pos)
    if window == 'doors':
        door.door_draw(screen, mouse_pos)
    if window == 'chest':
        my_chest.chest_draw(screen)
    if window == 'open_chest':
        my_chest.open_chest_draw(screen, loot)
        time.sleep(1)
        screen.fill('black')
        window = 'doors'
    if window == 'monster':
        if not move:
            for _ in range(1, 3):
                fight.fight_draw(screen, mouse_pos, move, attack, signal, miss)
                time.sleep(0.1)
        else:
            fight.fight_draw(screen, mouse_pos, move, attack, signal, miss)
    if window == 'game over':
        game_over.draw(screen, my_player.get_info())
        time.sleep(3)
        window = 'set record'
    if window == 'set record':
        game_over.draw(screen, my_player.get_info(), True, player_name)
    if window == 'records':
        records.records_draw(screen, mouse_pos, 'records.txt')
    if window == 'win':
        win.draw(screen, loot)
        time.sleep(3)
        window = 'doors'


    # если уровень с монстром
    if window == 'monster':
        # сброс сигналов 
        signal = 0
        miss = 0
        # если ход игрока
        if move:
            # обновляем данные в классе бой
            fight = monsters.Fight(my_player.get_info(), monster[rand_monster].get_info())
            # отслеживание событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    break
                # если нажата ЛКМ
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # если игрок атакует
                    if attack:
                        # атака по голове
                        if mouse_pos[0] in range(419, 596) and mouse_pos[1] in range(423, 450):
                            if not monster[rand_monster].give_damage('head'):
                                miss = 1
                            move = 0
                            attack = 0
                        # по корпусу
                        if mouse_pos[0] in range(419, 596) and mouse_pos[1] in range(463, 490):
                            if not monster[rand_monster].give_damage('body'):
                                miss = 1
                            move = 0
                            attack = 0
                        # по ногам
                        if mouse_pos[0] in range(419, 534) and mouse_pos[1] in range(503, 530):
                            if not monster[rand_monster].give_damage('legs'):
                                 miss = 1
                            move = 0
                            attack = 0
                        # назад
                        if mouse_pos[0] in range(419, 569) and mouse_pos[1] in range(543, 573):
                            attack = 0
                        # если враг убит
                        if monster[rand_monster].get_info()['health'] <= 0:
                            # меняем музыку
                            fight_sound.stop()
                            bg_sound.play()
                            # меняем уровень на победу
                            window = 'win'
                            loot = monster[rand_monster].get_loot()
                            my_player.get_loot(loot)
                            #screen.fill('black')
                            move = 1
                            attack = 0
                    # если игрок выбирает действие
                    else:
                        # атаковать
                        if mouse_pos[0] in range(419, 685) and mouse_pos[1] in range(443, 471):
                            attack = 1
                        # использовать зелье
                        if mouse_pos[0] in range(419, 775) and mouse_pos[1] in range(503, 530):
                            # если зелий нет
                            if not my_player.use_health_potion():
                                signal = 1
                            else:
                                move = 0
                                attack = 0
                    cycle = True
            # обновляем данные в классе бой
            fight = monsters.Fight(my_player.get_info(), monster[rand_monster].get_info())
        # если ход противника
        else:
            # дополнительная итерация цикла для проигрывания анимации
            if cycle:
                cycle = False
                continue
            # противник атакует
            damage = monster[rand_monster].get_damage()
            # попадание 
            if damage:
                my_player.damage(damage)
                # если игрок умирает
                if my_player.get_health_points() <= 0:
                    window = 'game over'
                    fight_sound.stop()
                    bg_sound.play()
            # промах
            else:
                miss = 1
            # передаем ход игроку
            move = 1
            # обновляем данные в классе бой
            fight = monsters.Fight(my_player.get_info(), monster[rand_monster].get_info())
            continue

    # отслеживание событий
    for event in pygame.event.get():
        # если тип события - нажатие на крестик - закрываем игру
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    
        # если открыто меню
        if window == 'menu':
            # если тип события - нажатие ЛКМ
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = start.menu_event(mouse_pos)
                # нажатие на кнопку "Играть"
                if click == 1:
                    # чистка экрана
                    screen.fill('black')
                    # окно дверей
                    window = 'doors'
                    break
                # нажатие на кнопку "Рекорды"
                if click == 2:
                    window = 'records'
                    break
                # нажатие на кнопку "Выход"
                if click == 3:
                    pygame.quit()
                    running = False

        # если открыто окно уровня с дверьми
        if window == 'doors':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if door.open_door(mouse_pos):
                    screen.fill('black')
                    window = door.open_door(mouse_pos)
                    #window = 'monster'
                    door = level_doors.Door()
                    if window == 'monster':
                        # отключаем фоновую музыку
                        bg_sound.stop()
                        # включаем музыку битвы
                        fight_sound.play()
                        rand_monster = random.randint(0, 5) 
                        monster[rand_monster].update()
                        move = 1
                        attack = 0
                    break
        
        # если уровень с сундуком
        if window == 'chest':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] in range(265, 508) and mouse_pos[1] in range(175, 417):
                    loot = my_chest.get_loot()
                    my_player.get_loot(loot)
                    my_player.get_info()
                    my_chest = chest.Chest()
                    window = 'open_chest'
                    screen.fill('black')
                    break
        
        # если открыто окно установления рекорда
        if window == 'set record':
            # ввод никнейма
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    continue
                if event.key == pygame.K_RETURN:
                    if count_symbols == 3:
                        # сохранение данных в файл
                        file = open('records.txt', 'a')
                        file.write(player_name + ' ' + str(my_player.get_info()['money']) + '\n')
                        file.close()
                        # сортировка данных по убыванию
                        sort_records.sort_records('records.txt')
                        # сброс текущих игровых данных
                        player_name = ''
                        count_symbols = 0
                        my_player = player.Player()
                        window = 'records'
                elif event.key == pygame.K_BACKSPACE:
                    if count_symbols > 0:
                        player_name = player_name[0:len(player_name) - 1]
                        count_symbols -= 1
                else:
                    if count_symbols < 3:
                        player_name += event.unicode
                        player_name = player_name.upper()
                        count_symbols += 1
        if window == 'records':
            if mouse_pos[0] in range(270, 470) and mouse_pos[1] in range(527, 568):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    window = 'menu'