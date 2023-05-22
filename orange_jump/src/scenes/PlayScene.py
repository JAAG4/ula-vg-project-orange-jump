import pygame

from gale.input_handler import InputHandler, InputData
from gale.text import render_text
from gale.timer import Timer

import settings
from src.Camera import Camera
from src.objects.Level import Level
from src.actors.player.PlayerEntity import Player
from gale.state_machine import BaseState


class PlayState(BaseState):
    def enter(self, **enter_kwargs) -> None:
        self.levelobj: Level = enter_kwargs.get(
            "level", Level(**settings.LEVELS_DEFAULT_CONFIG)
        )
        # self.surface: pygame.Surface = enter_kwargs["surface"]
        # self.levelobj.render(self.surface)
        pygame.mixer.music.load(settings.DEFAULT_SONG)
        pygame.mixer.music.play(-1)
        try:
            player_spawn = self.levelobj.entities["playerspawn"]
            spawn_x, spawn_y = player_spawn.px
        except Exception:
            spawn_x, spawn_y = (
                settings.VIRTUAL_WIDTH // 2,
                settings.VIRTUAL_HEIGHT // 2,
            )
        self.player = enter_kwargs.get(
            "player",
            Player(
                spawn_x,
                spawn_y,
                32,
                32,
                "orange",
            ),
        )
        self.camera = enter_kwargs.get(
            "camera",
            Camera(
                0,
                0,
                settings.VIRTUAL_WIDTH,
                settings.VIRTUAL_HEIGHT,
            ),
        )
        self.player.change_state("walk")

    def exit(self) -> None:
        InputHandler.unregister_listener(self)

    def update(self, dt: float) -> None:
        self.player.update(dt)
        self.camera.x = 0
        self.camera.y = self.player.y
        # self.levelobj.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        world_surf = pygame.Surface((self.levelobj.width, self.levelobj.height))
        self.levelobj.render(world_surf)
        self.player.render(world_surf)
        surface.blit(world_surf, (-self.camera.x, -self.camera.y))

        # render_text = # Timer goind up

    def on_input(self, input_id: str, input_data: InputData) -> None:
        # raise NotImplementedError
        pass
