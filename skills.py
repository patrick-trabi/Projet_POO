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

def defense_effect(user, target):
    #génère un bouclier temporaire 
    shield_value = user.speed // 2 + random.randint(5, 10)  # Calcul du bouclier
    if hasattr(target, "shield"):
        target.shield += shield_value  # Ajoute au bouclier existant
    else:
        target.shield = shield_value  # Crée un bouclier si inexistant
    print(f"{target.name} génère un bouclier de {shield_value} points.")
    
# Compétences
class Fireball(Skill):
    def __init__(self):
        super().__init__("Fireball", power=10, range=3, aoe=1, effect=attack_effect)

class Shield(Skill):
    def __init__(self):
        super().__init__("Shield", power=0, range=0, zone=0, effect=defense_effect)
