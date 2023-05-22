import pygame

from gale.input_handler import InputHandler, InputData
from gale.text import render_text
from gale.timer import Timer
from src.LDtk import  EntityInstance

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

    def check_wincon(self,end:EntityInstance):
        # end:EntityInstance = self.levelobj.entities.get("end")
        end_rect = pygame.Rect(left=end.px[0],top=end.px[1],height=end.height,width=end.width)
        if end_rect.contains(self.player.rect)
            

    def update(self, dt: float) -> None:
        # * Remember : Level :: self.coll_image
        # * Remember : Level :: self.coll_mask
        self.check_wincon(self)
        self.player.update(dt)
        self.camera.x = 0
        self.camera.y = self.player.y - (settings.VIRTUAL_HEIGHT // 3 * 2)

        offset_x = self.levelobj.x - self.player.x
        offset_y = self.levelobj.y - self.player.y

        overlaps, magni = self.player.mask.overlap(
            self.levelobj.coll_mask, offset=(offset_x, offset_y)
        ), self.player.mask.overlap_area(
            self.levelobj.coll_mask, offset=(offset_x, offset_y)
        )
        # print(overlaps, magni)
        if not overlaps:
            self.player.will_fall = True
        if overlaps:
            self.player.will_fall = False
            self.player.y += overlaps[1] - self.player.height
            self.player.y_vel = 0

    def render(self, surface: pygame.Surface) -> None:
        world_surf = pygame.Surface((self.levelobj.width, self.levelobj.height))
        self.levelobj.render(world_surf)
        self.player.render(world_surf)
        surface.blit(world_surf, (-self.camera.x, -self.camera.y))

        # render_text = # Timer goind up
