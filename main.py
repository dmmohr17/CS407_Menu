import pygame
from game_start.bootstrap_stage import BootStrapStage
from pick_characters.pick_characters_stage import PickCharactersStage
from map_select.pick_map_stage import PickMapStage
from gameplay.gameplay_stage import GamePlayStage
from game_over.game_over_stage import GameOverStage

def create_stage(stage_name, data):
    if stage_name == "BOOTSTRAP":
        return BootStrapStage(**data)
    elif stage_name == "PICK_MAP":
        return PickMapStage(**data)
    elif stage_name == "PICK_CHARACTERS":
        return PickCharactersStage(**data)
    elif stage_name == "GAMEPLAY":
        return GamePlayStage(**data)
    elif stage_name == "GAME_OVER":
        return GameOverStage(**data)
    
    # pyinstaller --onefile --noconsole --add-data "pick_characters/DIMIS___.TTF;pick_characters" --add-data "image_reference/chars/*.*;image_reference/chars" --add-data "image_reference/sounds/*.*;image_reference/sounds" --add-data "image_reference/background/*.*;image_reference/background" main.py

current_stage = BootStrapStage()
#current_stage = GamePlayStage('name_of_the_wind', 'throwing_knife', 'Starry Space', arena=False, lives=3)

running = True

while running:
    result = current_stage.updateGameplay()

    if result is not None:
        stage_name, data = result
        current_stage = create_stage(stage_name, data)