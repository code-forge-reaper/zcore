## Table of Contents


- [draw](#draw)

- [helpers](#helpers)

- [keys](#keys)

- [obj](#obj)

- [window](#window)

# zcore API Reference


## `draw`


drawing module, you can also just manualy
write each function yourself if you want finer control


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

this draws a circle with no fill


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

this is a rectangle made of lines, no fill


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

this is useful when you are running on low memory devices, where you can't keep loading the same resource


```python
memFree(fn)
```

this decorator forces python's GC to run


```python
memUsageGet(fn)
```

this decorator returns the memory used by a function, as well as it's return value


```python
nonWorking(reason: str = None)
```

this is just a way we do things internally, since it's easier to ctrl-f it


```python
timeit(fn)
```

this is a debug decorator, used to measure how long a function takes to run


## `keys`


keys.py

This defines keyboard constants that you can use.


## `obj`


a simple script that contains useful classes


### Classes


### class `SpriteObject`

Represents a sprite that can be drawn to the screen.

#### `draw(self, surface: pygame.surface.Surface, x: int, y: int, scaleX: int, scaleY: int)`

this draws the sprite object


## `window`


this contains the main loop of the application


### Functions


```python
createWindow(width: int, height: int, title: str) -> pygame.surface.Surface
```

this creates a window and returns it
Args:
    width: the width of the window
    height: the height of the window
    title: the title of the window

Returns:
    window: a instance of pygame.Surface


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
    key: the name of the key you want to check

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

sets running to false
making the main loop exit
