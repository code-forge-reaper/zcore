"""
a simple script that contains useful classes
"""
import pygame


class SpriteObject:
    """Represents a sprite that can be drawn to the screen."""

    def __init__(self, sprite_path: str):
        self.sprite_path = sprite_path
        self.sprite = pygame.image.load(sprite_path)

    def draw(self, surface: pygame.Surface, x: int, y: int, scaleX: int, scaleY: int):
        """
            this draws the sprite object
        """
        pos = pygame.Vector2(x, y)
        rect = self.sprite.get_rect(center=(pos.x, pos.y))

        surface.blit(
            pygame.transform.scale(self.sprite, (scaleX, scaleY)), rect.topleft
        )
