from typing import Any, Dict, Tuple
from gale.input_handler import InputHandler, InputData
from gale.state_machine import StateMachine

import settings
from src.actors.BaseState import BaseEntityState


class GroundedState(BaseEntityState):
    def __init__(self, entity, state_machine: StateMachine) -> None:
        super().__init__(entity, state_machine)

    def enter(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        self.entity.sprite_flipped = True if kwargs.get("direction") else False

        self.entity.change_animation("walk")
        InputHandler.register_listener(self)

    def exit(self):
        InputHandler.unregister_listener(self)

    def update(self, *args):
        if self.entity.will_fall:
            self.entity.change_state("fall")

    def on_input(self, input_id: str, input_data: InputData):
        pass
