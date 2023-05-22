import pygame
from src.actors.Mixins import AnimatedMixin
from gale.state_machine import StateMachine, BaseState
from typing import Dict, Any, Tuple
import settings
from src.actors.player.states.Walk import GroundedState

# from src.actors.player.states.Idle import IdleState
# from src.actors.player.states.Jump import JumpState
from src.actors.player.states.Fall import FallState


DEFAULT_ANIMATIONS = {
    "idle": {"frames": [0, 1, 2, 3], "interval": 0.2},
    "walk": {"frames": [12, 13, 14, 15, 16, 17], "interval": 0.2},
    "jump": {"frames": [18]},
    "fall": {"frames": [19, 20], "interval": 0.1},
}


class Entity(pygame.sprite.Sprite, AnimatedMixin):
    COLOR = (0, 0, 255)

    def __init__(self, x, y, width, height, texture_key, states, animation_defs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_vel = 0
        self.y_vel = 0

        self.rect = pygame.Rect(x, y, width, height)
        self.mask = None
        self.sprite_flipped = False
        self.texture_key = texture_key
        self.frame_index = -1
        self.state_machine = StateMachine(states)
        self.animations = {}
        self.generate_animations(animation_defs)  # ?populates self.animations
        self.will_fall = False
        frame = settings.FRAMES[self.texture_key][self.frame_index]
        self.image = pygame.Surface((frame.width, frame.height), pygame.SRCALPHA)
        self.mask = pygame.mask.from_surface(self.image)

    def change_state(
        self, state_id: str, *args: Tuple[Any], **kwargs: Dict[str, Any]
    ) -> None:
        self.state_machine.change(state_id, *args, **kwargs)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)
        AnimatedMixin.update(self, dt)
        if self.x <= self.width and self.x_vel < 0:
            self.x = max(0, self.x)
        elif self.x >= settings.MAX_WIDTH + 1:
            self.x = min(settings.MAX_WIDTH - self.width, self.x)

    def render(self, surface: pygame.Surface):
        texture = settings.TEXTURES[self.texture_key]
        frame = settings.FRAMES[self.texture_key][self.frame_index]
        image = pygame.Surface((frame.width, frame.height), pygame.SRCALPHA)
        image.fill(color=(0, 0, 0, 0))
        image.blit(texture, (0, 0), frame)
        if self.sprite_flipped:
            image = pygame.transform.flip(image, True, False)
        self.image = image
        self.mask = pygame.mask.from_surface(image)
        surface.blit(image, (self.x, self.y))


class Player(Entity):
    def __init__(
        self,
        x,
        y,
        width=32,
        height=32,
        texture_key="orange",
        states={},
        animation_defs=DEFAULT_ANIMATIONS,
    ):
        self.current_animation = None
        self.frame_index = None
        states = {
            # "idle": lambda sm: IdleState(self, sm),
            "walk": lambda sm: GroundedState(self, sm),
            # "jump": lambda sm: JumpState(self, sm),
            "fall": lambda sm: FallState(self, sm),
        }
        self.will_fall = False
        super().__init__(x, y, width, height, texture_key, states, animation_defs)

    def move(self, dt):
        self.x += round(self.x_vel * dt)
        self.y += round(self.y_vel * dt)

    def update_sprite_dir(self):
        if self.x_vel < 0:
            self.sprite_flipped = True

    def update(self, dt):
        super(Player, self).update(dt)
        self.move(dt)
        self.update_sprite_dir()
