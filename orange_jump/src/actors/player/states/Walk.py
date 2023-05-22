from typing import Any, Dict, Tuple
from gale.input_handler import InputHandler, InputData
from gale.state_machine import StateMachine

import settings
from src.actors.BaseState import BaseEntityState
import pygame


class GroundedState(BaseEntityState):
    def __init__(self, entity, state_machine: StateMachine) -> None:
        super().__init__(entity, state_machine)

    def enter(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        self.entity.sprite_flipped = True if kwargs.get("direction") else False
        self.entity.y_vel = 0
        self.entity.change_animation("walk")
        InputHandler.register_listener(self)

    def exit(self):
        InputHandler.unregister_listener(self)

    def update(self, *args):
        if self.entity.will_fall:
            self.entity.change_state("fall")
        if self.entity.x_vel == 0:
            self.entity.change_animation("idle")

    def on_input(self, input_id: str, input_data: InputData) -> None:
        # raise NotImplementedError
        input_move_left = False
        input_move_right = False
        for key in settings.PYGAME_RAW_INPUT["move_left"]:
            input_move_left |= key in pygame.key.get_pressed()
        for key in settings.PYGAME_RAW_INPUT["move_right"]:
            input_move_right |= key in pygame.key.get_pressed()
        if input_move_left and input_move_right:
            return
        if input_move_left or input_id == "move_left":
            if input_move_left or input_data.pressed:
                self.entity.x_vel = -settings.PLAYER_WALK_PPX
                self.entity.sprite_flipped = True
            elif input_data.released:
                self.entity.change_animation("idle")
                self.entity.x_vel = 0

        if input_move_right or input_id == "move_right":
            if input_move_right or input_data.pressed:
                self.entity.x_vel = settings.PLAYER_WALK_PPX
                self.entity.sprite_flipped = False
            elif input_data.released and self.entity.x_vel >= 0:
                self.entity.change_animation("idle")
                self.entity.x_vel = 0

        if input_id == "jump" and input_data.pressed:
            self.entity.change_state("jump")
