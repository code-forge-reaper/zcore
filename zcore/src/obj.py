from .vec2 import Vec2
import pygame


class SpriteObject:
    def __init__(self, sprite_path: str):
        self.sprite_path = sprite_path
        self.sprite = pygame.image.load(sprite_path)

    def draw(self, surface: pygame.Surface, x: int, y: int, scaleX: int, scaleY: int):
        pos = Vec2(x, y)
        rect = self.sprite.get_rect(center=(pos.x, pos.y))

        surface.blit(
            pygame.transform.scale(self.sprite, (scaleX, scaleY)), rect.topleft
        )
