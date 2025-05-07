import pygame

type ColorType = tuple[int, int, int, int] | pygame.Color | str


def clearBackground(window: pygame.Surface, color: ColorType) -> None:
    """
    Clears the background with the specified color.

    Args:
        window: The window surface.
        color: The color to fill the background.
    """
    window.fill(color)


def fillRect(
    screen: pygame.Surface, x: int, y: int, width: int, height: int, color: ColorType
) -> None:
    """
    Draws a rectangle on the screen.

    Args:
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        color (ColorType): The color of the rectangle.

    Returns:
        None
    """
    pygame.draw.rect(screen, color, (x, y, width, height))


def fillCircle(
    surface: pygame.Surface, color: ColorType, center: tuple[int, int], radius: int
) -> None:
    """
    Draws a filled circle on the surface.

    Args:
        surface: The surface to draw on.
        color: The color of the circle.
        center: The center coordinates of the circle.
        radius: The radius of the circle.
    """
    pygame.draw.circle(surface, color, center, radius)


def drawLine(
    surface: pygame.Surface,
    color: ColorType,
    start_pos: tuple[int, int],
    end_pos: tuple[int, int],
    width: int = 1,
) -> None:
    """
    Draws a line on the surface.

    Args:
        surface: The surface to draw on.
        color: The color of the line.
        start_pos: The starting coordinates of the line.
        end_pos: The ending coordinates of the line.
        width: The width of the line (default is 1).
    """
    pygame.draw.line(surface, color, start_pos, end_pos, width)


def drawText(
    window: pygame.Surface, text: str, x: int, y: int, size: int, color: ColorType
) -> None:
    """
    Renders text on the surface.

    Args:
        window: The window surface.
        text: The text string to render.
        x (int): The x-coordinate of the top-left corner of the text.
        y (int): The y-coordinate of the top-left corner of the text.
        size (int): The font size of the text.
        color (ColorType): The color of the text.
    """
    font = pygame.font.Font(None, size)
    textSurface = font.render(text, True, color)
    window.blit(textSurface, (x, y))


def drawRect(
    screen: pygame.Surface, x: int, y: int, width: int, height: int, color: ColorType
) -> None:
    # this is a rectangle made of lines, no fill
    pygame.draw.rect(screen, color, (x, y, width, height), 1)


def drawCircle(
    surface: pygame.Surface, color: ColorType, center: tuple[int, int], radius: int
) -> None:
    pygame.draw.circle(surface, color, center, radius, 1)
