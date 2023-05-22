from typing import Any, Dict, Tuple
from gale.input_handler import InputHandler, InputData
from gale.state_machine import StateMachine

import settings
from src.actors.BaseState import BaseEntityState
import pygame


class JumpState(BaseEntityState):
    def __init__(self, entity, state_machine: StateMachine) -> None:
        super().__init__(entity, state_machine)
        self.PLAYER_JUMP_X_CTRL_RATE = settings.PLAYER_JUMP_X_CTRL_RATE
        self.can_double_jump = True

    def enter(self):
        self.entity.change_animation("jump")
        self.entity.y_vel -= settings.GRAVITY_PPX * 1 + 2
        InputHandler.register_listener(self)
        self.can_double_jump = True
        self.PLAYER_JUMP_X_CTRL_RATE = settings.PLAYER_JUMP_X_CTRL_RATE

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        self.entity.y_vel += settings.GRAVITY_PPX * dt
        # self.entity.update(dt)
        if self.entity.y_vel >= 0:
            self.entity.change_state("fall")

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.entity.x_vel = (
                    -settings.PLAYER_WALK_PPX * self.PLAYER_JUMP_X_CTRL_RATE
                )
                self.entity.flipped = True
            elif input_data.released and self.entity.x_vel <= 0:
                self.entity.x_vel = 0

        elif input_id == "move_right":
            if input_data.pressed:
                self.entity.x_vel = (
                    settings.PLAYER_WALK_PPX * self.PLAYER_JUMP_X_CTRL_RATE
                )
                self.entity.flipped = False
            elif input_data.released and self.entity.x_vel >= 0:
                self.entity.x_vel = 0
        elif input_id == "jump" and self.can_double_jump:
            if input_data.pressed:
                self.can_double_jump = False
                self.entity.y_vel -= settings.GRAVITY_PPX * 0.7
                self.PLAYER_JUMP_X_CTRL_RATE = 1.1
                self.entity.change_animation("double_jump")
