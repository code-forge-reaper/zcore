## Table of Contents


- [draw](#draw)

- [helpers](#helpers)

- [keys](#keys)

- [mouse](#mouse)

- [obj](#obj)

- [vec2](#vec2)

- [window](#window)

# zcore API Reference


## `draw`


_no module docstring_


### Functions


```python
clearBackground(window: pygame.surface.Surface, color: ColorType) -> None
```

Clears the background with the specified color.

Args:
    window: The window surface.
    color: The color to fill the background.


```python
drawCircle(surface: pygame.surface.Surface, color: ColorType, center: tuple[int, int], radius: int) -> None
```

_no docstring_


```python
drawLine(surface: pygame.surface.Surface, color: ColorType, start_pos: tuple[int, int], end_pos: tuple[int, int], width: int = 1) -> None
```

Draws a line on the surface.

Args:
    surface: The surface to draw on.
    color: The color of the line.
    start_pos: The starting coordinates of the line.
    end_pos: The ending coordinates of the line.
    width: The width of the line (default is 1).


```python
drawRect(screen: pygame.surface.Surface, x: int, y: int, width: int, height: int, color: ColorType) -> None
```

_no docstring_


```python
drawText(window: pygame.surface.Surface, text: str, x: int, y: int, size: int, color: ColorType) -> None
```

Renders text on the surface.

Args:
    window: The window surface.
    text: The text string to render.
    x (int): The x-coordinate of the top-left corner of the text.
    y (int): The y-coordinate of the top-left corner of the text.
    size (int): The font size of the text.
    color (ColorType): The color of the text.


```python
fillCircle(surface: pygame.surface.Surface, color: ColorType, center: tuple[int, int], radius: int) -> None
```

Draws a filled circle on the surface.

Args:
    surface: The surface to draw on.
    color: The color of the circle.
    center: The center coordinates of the circle.
    radius: The radius of the circle.


```python
fillRect(screen: pygame.surface.Surface, x: int, y: int, width: int, height: int, color: ColorType) -> None
```

Draws a rectangle on the screen.

Args:
    x (int): The x-coordinate of the rectangle.
    y (int): The y-coordinate of the rectangle.
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    color (ColorType): The color of the rectangle.

Returns:
    None


## `helpers`


each function in this file is supposed to be used as a decorator
example:

from helpers import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


### Functions


```python
cache(fn)
```

_no docstring_


```python
memFree(fn)
```

_no docstring_


```python
memUsageGet(fn)
```

_no docstring_


```python
nonWorking(reason: str = None)
```

_no docstring_


```python
timeit(fn)
```

this is a debug decorator, used to measure how long a function takes to run


## `keys`


keys.py

This defines keyboard constants that you can use.


## `mouse`


_no module docstring_


## `obj`


_no module docstring_


### Classes


### class `SpriteObject`

_no docstring_

#### `draw(self, surface: pygame.surface.Surface, x: int, y: int, scaleX: int, scaleY: int)`

_no docstring_


## `vec2`


_no module docstring_


### Classes


### class `Vec2`

_no docstring_

#### `copy(self) -> 'Vec2'`

_no docstring_


## `window`


_no module docstring_


### Functions


```python
createWindow(width: int, height: int, title: str) -> pygame.surface.Surface
```

this creates a window,
Args:
    width: the width of the window
    height: the height of the window
    title: the title of the window


```python
isKeyDown(key: int) -> bool
```

Checks if a key is currently pressed down.

Args:
    key: The key code.

Returns:
    bool: True if the key is pressed, False otherwise.


```python
isKeyPressed(key: int) -> bool
```

Checks if the key was just pressed

Args:
    key(str): the name of the key you want to check

Returns:
    bool: True if the key was just clicked, False otherwise


```python
mainLoop(gameLoop: Callable)
```

Main loop for the game.

Args:
    gameLoop: A callable that represents the game loop, which takes the delta time as an argument.


```python
quit() -> None
```

_no docstring_
