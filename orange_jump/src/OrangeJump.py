"""
This module was autogenerated by gale.
"""
from typing import Any, Dict, Optional, Tuple, Union
import pygame

from gale.game import Game
from gale.input_handler import InputData, InputHandler
from gale.state_machine import StateMachine

# from src.scenes.StartMenuScene import StartMenuScene
from src.scenes.PlayScene import PlayState

from src.scenes.EndScene import EndScene


class OrangeJump(Game):
    def __init__(
        self,
        title: Union[str, None] = None,
        window_width: int = 800,
        window_height: int = 600,
        virtual_width: Union[int, None] = None,
        virtual_height: Union[int, None] = None,
        fps: int = 60,
        *args: Tuple[Any],
        **kwargs: Dict[str, Any]
    ) -> None:
        super().__init__(
            title,
            window_width,
            window_height,
            virtual_width,
            virtual_height,
            fps,
            *args,
            **kwargs
        )

    def init(self) -> None:
        self.state_machine = StateMachine(
            {
                # "start_menu": StartMenuScene,
                "play": PlayState,
                "end": EndScene,
            }
        )
        self.state_machine.change("play")
        # self.state_machine.change("start_menu")
        InputHandler.register_listener(self)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, render_surface: pygame.Surface) -> None:
        self.state_machine.render(render_surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_data.pressed and input_id == "quit":
            self.quit()
