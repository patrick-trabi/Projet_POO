import random

class Skill:
    def __init__(self, name, power, range,zone, effect):
        self.name = name
        self.power = power
        self.range = range  # Portée en cases
        self.zone = zone # 1 pour une seule case en zone d'effet
        self.effect = effect  # Fonction d'effet (attaque, defense, etc.)

    def use(self, user, target):
        self.effect(user, target)

# Effets spécifiques pour les compétences
def attack_effect(user, target):
    damage = user.attack + random.randint(0, 5)
    target.take_damage(damage)


# Compétences
class Fireball(Skill):
    def __init__(self):
        super().__init__("Fireball", power=10, range=3, aoe=1, effect=attack_effect)


