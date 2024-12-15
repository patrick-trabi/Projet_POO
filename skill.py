import random

class Skill:
    """
    Classe pour représenter une compétence.
    """
    def __init__(self, name, power, range, zone, effect):
        """
        Initialise une compétence avec un nom, une puissance, une portée et un effet.

        Paramètres
        ----------
        name : str
            Le nom de la compétence.
        power : int
            La puissance de la compétence.
        range : int
            La portée en cases.
        zone : int
            La zone d'effet (nombre de cases affectées).
        effect : function
            La fonction définissant l'effet de la compétence.
        """
        self.name = name
        self.power = power
        self.range = range  # Portée en cases
        self.zone = zone    # Zone d'effet (1 pour une seule case, >1 pour AoE)
        self.effect = effect  # Fonction d'effet (attaque, défense, soin, etc.)

    def use(self, user, targets):
        """
        Utilise la compétence sur les cibles spécifiées.

        Paramètres
        ----------
        user : Unit
            L'unité qui utilise la compétence.
        targets : list[Unit]
            Les unités ciblées par la compétence.
        """
        for target in targets:
            self.effect(user, target)

# Effets spécifiques pour les compétences
def attack_effect(user, target):
    """
    Effet d'attaque : inflige des dégâts à la cible.

    Paramètres
    ----------
    user : Unit
        L'unité qui attaque.
    target : Unit
        L'unité ciblée.
    """
    damage = user.attack_power + random.randint(0, 5)
    target.health -= damage
    print(f"{user.team} inflige {damage} dégâts à {target.team} (PV restant : {target.health}).")

def defense_effect(user, target):
    """
    Effet défensif : génère un bouclier temporaire.

    Paramètres
    ----------
    user : Unit
        L'unité qui génère le bouclier.
    target : Unit
        L'unité qui reçoit le bouclier.
    """
    shield_value = user.speed // 2 + random.randint(5, 10)  # Calcul du bouclier
    if hasattr(target, "shield"):
        target.shield += shield_value  # Ajoute au bouclier existant
    else:
        target.shield = shield_value  # Crée un bouclier si inexistant
    print(f"{target.team} génère un bouclier de {shield_value} points.")

def heal_effect(user, target):
    """
    Effet de soin : restaure des points de vie à la cible.

    Paramètres
    ----------
    user : Unit
        L'unité qui effectue le soin.
    target : Unit
        L'unité soignée.
    """
    heal_amount = user.attack_power // 2 + random.randint(5, 10)
    target.health += heal_amount
    print(f"{user.team} soigne {heal_amount} PV pour {target.team} (PV actuel : {target.health}).")

# Compétences
class Fireball(Skill):
    def __init__(self):
        super().__init__(
            name="Fireball",
            power=10,
            range=3,
            zone=1,
            effect=attack_effect
        )

class Shield(Skill):
    def __init__(self):
        super().__init__(
            name="Shield",
            power=0,
            range=0,
            zone=0,
            effect=defense_effect
        )

class Slash(Skill):
    def __init__(self):
        super().__init__(
            name="Slash",
            power=15,
            range=1,
            zone=1,
            effect=attack_effect
        )

class Arrows(Skill):
    def __init__(self):
        super().__init__(
            name="Arrows",
            power=7,
            range=3,
            zone=3,
            effect=attack_effect
        )

class Heal(Skill):
    def __init__(self):
        super().__init__(
            name="Heal",
            power=0,  # Puissance n'est pas utilisée pour le soin
            range=3,  # Portée de soin
            zone=1,  # Une seule unité ciblée
            effect=heal_effect
        )

class Evasion(Skill):
    def __init__(self):
        super().__init__(
            name="Evasion",
            power=0,
            range=0,
            zone=0,
            effect=lambda user, target: print(f"{user.team} esquive une attaque.")
        )
