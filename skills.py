import random

class Skill:
    def __init__(self, name, power, range, zone, effect):
        self.name = name
        self.power = power
        self.range = range
        self.zone = zone
        self.effect = effect

    def use(self, user, target):
        self.effect(user, target)

# Effets spécifiques
def attack_effect(user, target):
    damage = user.attack_power + random.randint(0, 5)
    target.health -= damage
    target.effect_color = (255, 0, 0)  # Rouge pour un effet visuel temporaire
    target.effect_timer = 15  # Durée de l'effet en frames

def defense_effect(user, target):
    shield_value = user.attack_power // 2 + random.randint(5, 10)
    if hasattr(target, "shield"):
        target.shield += shield_value

def evasion_effect(user, target):
    if hasattr(target, "dodge_chance"):
        target.dodge_chance = min(100, target.dodge_chance + 20)

def slash_effect(user, target):
    if abs(user.x - target.x) <= 1 and abs(user.y - target.y) <= 1:
        damage = user.attack_power + random.randint(5, 10)
        target.health -= damage
        target.effect_color = (255, 0, 0)  # Rouge pour Slash
        target.effect_timer = 15

# Compétences
class Fireball(Skill):
    def __init__(self):
        self.name = "Fireball"
        self.power = 10
        self.range = 3
        self.zone = 1
        self.effect = attack_effect

class Shield(Skill):
    def __init__(self):
        self.name = "Shield"
        self.power = 0
        self.range = 0
        self.zone = 0
        self.effect = defense_effect

class Arrows(Skill):
    def __init__(self):
        self.name = "Arrows"
        self.power = 7
        self.range = 3
        self.zone = 3
        self.effect = attack_effect

class Evasion(Skill):
    def __init__(self):
        self.name = "Evasion"
        self.power = 0
        self.range = 0
        self.zone = 0
        self.effect = evasion_effect

class Slash(Skill):
    def __init__(self):
        self.name = "Slash"
        self.power = 15
        self.range = 1
        self.zone = 0
        self.effect = slash_effect

