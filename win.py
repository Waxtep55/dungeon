import pygame

def draw(screen, loot=False):
	screen.fill('black')
	font_win = pygame.font.Font('fonts/pixel.ttf', 60)
	text_win = font_win.render('Победа!', True, 'white')
	screen.blit(text_win, (216, 172))
	if loot:
		font_loot = pygame.font.Font('fonts/pixel.ttf', 40)
		text_loot = font_loot.render(f'Получено: x{loot}', True, 'white')
		if loot < 10:
			screen.blit(pygame.image.load('img/elements/health_potion.png'), (509, 300))
		else:
			screen.blit(pygame.image.load('img/elements/coin/coin_01.png'), (509, 300))
		screen.blit(text_loot, (159, 305))
	pygame.display.update()