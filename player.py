class Player:
    # задаем параметры игрока
    def __init__(self):
        self.health_points = 100
        self.money = 0
        self.health_potions = 0
    
    def get_health_points(self):
        return self.health_points

    # получить зелья здоровья
    def _get_health_potion(self, count):
        self.health_potions += count

    # получить деньги
    def _get_money(self, count):
        self.money += count
    
    def get_loot(self, loot):
        if loot == 'potion':
            Player._get_health_potion(self, 1)
            return 1
        elif loot < 10:
            Player._get_health_potion(self, loot)
            return 1
        else:
            Player._get_money(self, loot)
    
    def get_info(self):
        return {'health': self.health_points, 'money': self.money, 'potions': self.health_potions}

    # использовать зелье здоровья
    def use_health_potion(self):
        if self.health_potions > 0:
            if self.health_points >= 60:
                self.health_points = 100
            else:
                self.health_points += 40
            self.health_potions -= 1
            return 1
        else:
            return 0
    
    # урон
    def damage(self, count):
        self.health_points -= count
        if self.health_points <= 0:
            return 1
        else:
            return 0