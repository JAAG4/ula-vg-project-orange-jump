import pygame
from gale.text import render_text


import settings
from src.objects.Level import Level
from gale.state_machine import BaseState


class EndScene(BaseState):
    def enter(self, **enter_kwargs) -> None:
        pass
        # self.levelobj: Level = enter_kwargs.get(
        #     "level", Level(settings.LEVELS_DEFAULT_CONFIG["ldtkworldpath"], level_n=1)
        # )

    def render(self, surface: pygame.Surface) -> None:
        # self.levelobj.render(surface)
        render_text(
            surface,
            "THE END",
            color=pygame.Color(255, 255, 255),
            font=settings.FONTS["huge"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=settings.VIRTUAL_HEIGHT // 2,
            center=True,
            shadowed=True,
        )
