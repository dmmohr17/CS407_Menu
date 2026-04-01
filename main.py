import pygame
from map_select.pick_map_stage import PickMapStage
from gameplay.gameplay_stage import GamePlayStage
from game_over.game_over_stage import GameOverStage

def create_stage(stage_name, data):
    if stage_name == "PICK_MAP":
        return PickMapStage(**data)
    elif stage_name == "GAMEPLAY":
        return GamePlayStage(**data)
    elif stage_name == "GAME_OVER":
        return GameOverStage(**data)

current_stage = PickMapStage(arena=True)

running = True

while running:
    result = current_stage.updateGameplay()

    if result is not None:
        stage_name, data = result
        current_stage = create_stage(stage_name, data)