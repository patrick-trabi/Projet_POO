import pygame
import random

CELL_SIZE = 40
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TREE_COLOR = (34, 139, 34)
WALL_COLOR = (139, 69, 19)

class Interface:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.grid_width = width // CELL_SIZE
        self.grid_height = height // CELL_SIZE
        self.obstacles = self.generate_obstacles()

        # Backgrounds pour l'accueil et la sélection
        self.background_home = pygame.image.load("main.jpg").convert()
        self.background_home = pygame.transform.scale(self.background_home, (width, height))
        self.background_selection = pygame.image.load("selection.jpg").convert()
        self.background_selection = pygame.transform.scale(self.background_selection, (width, height))

        # Terrain du jeu
        self.background = pygame.image.load("field.jpg").convert()

    def generate_obstacles(self):
        obstacles = []
        for _ in range(20):
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            obstacles.append((x, y, random.choice(["tree", "wall"])))
        return obstacles

    def show_home_screen(self):
        """Affiche l'écran d'accueil avec un bouton 'Play'."""
        font = pygame.font.Font(None, 72)
        running = True

        while running:
            self.screen.blit(self.background_home, (0, 0))  # Affiche le background de l'accueil
            text = font.render("Press ENTER to Play", True, BLACK)
            self.screen.blit(text, (self.width // 2 - 200, self.height // 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Touche Entrée pour jouer
                    running = False

    def show_unit_selection(self):
        #Affiche un écran de sélection d'unités
        font = pygame.font.Font(None, 36)
        unit_names = ["Ninja", "Samurai", "Archer"]
        current_index = 0  # Index de l'unité en cours
        selected_units = []

        while len(selected_units) < 2:
            self.screen.blit(self.background_selection, (0, 0))  # Affiche le background de la sélection

            # Affiche les unités avec la couleur de sélection
            for idx, name in enumerate(unit_names):
                color = (0, 255, 0) if idx == current_index else WHITE  # Vert si sélectionné
                text = font.render(name, True, color)
                self.screen.blit(text, (self.width // 4 * (idx + 1) - 50, self.height // 2))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  # Flèche gauche
                        current_index = (current_index - 1) % len(unit_names)
                    elif event.key == pygame.K_RIGHT:  # Flèche droite
                        current_index = (current_index + 1) % len(unit_names)
                    elif event.key == pygame.K_RETURN:  # Touche Entrée pour sélectionner une unité
                        selected_units.append(unit_names[current_index])
                        print(f"Vous avez sélectionné : {unit_names[current_index]}")

        return selected_units

    def draw_grid(self):
        self.screen.blit(self.background, (0, 0))
        for x in range(0, self.width, CELL_SIZE):
            for y in range(0, self.height, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

    def draw_obstacles(self):
        for x, y, obstacle_type in self.obstacles:
            color = TREE_COLOR if obstacle_type == "tree" else WALL_COLOR
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, color, rect)

    def draw_units(self, player_units, enemy_units):
        for unit in player_units + enemy_units:
            unit.draw(self.screen)

    def highlight_targets(self, screen, targets, current_index):
        #Surligne les cibles disponibles et indique la cible actuellement sélectionnée
        for i, target in enumerate(targets):
            color = (255, 0, 0) if i == current_index else (255, 255, 0)
            rect = pygame.Rect(target.x * CELL_SIZE, target.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect, 3)

    def draw_skills(self, unit):
        if not unit.skills:
            return

        font = pygame.font.Font(None, 24)
        skill_text = "Skills: "
        for idx, skill in enumerate(unit.skills):
            skill_text += f"{idx + 1} - {skill.name}  "

        skill_surface = font.render(skill_text, True, (255, 255, 255))
        self.screen.blit(skill_surface, (10, self.height - 30))

    def flip_display(self, player_units, enemy_units):
        self.draw_grid()
        self.draw_obstacles()
        self.draw_units(player_units, enemy_units)
        selected_unit = next((unit for unit in player_units if unit.is_selected), None)
        if selected_unit:
            self.draw_skills(selected_unit)
        pygame.display.flip()  
