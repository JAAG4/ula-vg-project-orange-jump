import pygame
from typing import Any, List
from src.LDtk import ldtk_from_file
import os
from pathlib import Path
from settings import BASE_DIR


class Level(pygame.sprite.Sprite):
    def __init__(
        self,
        ldtkworldpath: str,
        level_n: int = 0,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        _ldtkinfo = ldtk_from_file(ldtkworldpath)
        lv = _ldtkinfo.levels[level_n]
        self.height = lv.px_hei
        self.width = lv.px_wid
        self.name = lv.identifier
        self.bg_path = lv.bg_rel_path.replace("..", "assets")
        coll_layer = None
        self.layers_imgs = []
        layers_imgs = []
        _layers = []
        for lyr in lv.layer_instances[::-1]:
            _lyr = {}
            _lyr["grid_size"] = lyr.grid_size
            try:
                _lyr["tileset_path"] = lyr.tileset_rel_path.replace("..", "assets")
            except Exception as e:
                pass
                # print("layer>>", e)
            _lyr["rows"] = lyr.c_hei
            _lyr["cols"] = lyr.c_wid
            if lyr.entity_instances:
                # ! Assumed Single Entity Layer!!
                self.entities = {}
                for ent in lyr.entity_instances:
                    self.entities[ent.identifier] = ent
            _layers.append(_lyr)
        for lyr in os.listdir(BASE_DIR / "assets" / "ldtk" / "World" / "png"):
            layers_imgs.append(
                (
                    lyr,
                    pygame.image.load(
                        BASE_DIR / "assets" / "ldtk" / "World" / "png" / lyr
                    ),
                )
            )
        self.layers_imgs = layers_imgs
        self.coll_image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.coll_mask = pygame.mask.from_surface(self.coll_image)

    def get_layer_png_paths(self) -> List[str]:
        _layers = []
        for png in os.listdir(BASE_DIR / "assets" / "ldtk" / "World" / "png"):
            if self.name in png and "-int" not in png:
                _layers.append(png)
        return _layers

    def render(self, surface: pygame.Surface):
        for layer, layerimg in self.layers_imgs:
            surface.blit(layerimg, (self.x, self.y))
            if "main" in layer:
                self.coll_image = pygame.Surface.copy(layerimg)
                # self.coll_mask = pygame.mask.from_surface(self.coll_image)
                self.coll_mask = pygame.mask.from_surface(layerimg)
