from pygame.math import Vector2
import zcore, random, pygame
from zcore.src.draw import drawText
from zcore.src.helpers import cache

win = zcore.window.createWindow(800,600,"outpost: null")

# this automatically makes the function more memory efficient
# as in:
# 	it stores the result that was returned, using the arguments as the key
#	if it can actualy find the arguments, it returns the value that was stored
# 	otherwise it runs the function and stores the result
@cache
def loadImage(path:str) -> pygame.Surface:
	print(f"loading: {path}")
	return pygame.image.load(path)

background = loadImage("image.jpg")
background = loadImage("image.jpg")# won't be re-executed, but will get the value from the first call

player = Vector2()
coin = Vector2(
	random.randint(200,win.get_width()-200),
	random.randint(200,win.get_height()-200)
)

points = 0

def move(dt: float) -> None:
	global points
	# this reminds me how i did input when i tried to make a game using godot
	player.y -= (zcore.window.isKeyDown(zcore.keys.KEY_W)-zcore.window.isKeyDown(zcore.keys.KEY_S))*200 * dt
	player.x -= (zcore.window.isKeyDown(zcore.keys.KEY_A)-zcore.window.isKeyDown(zcore.keys.KEY_D))*200 * dt

	# simulation: if W is down, and S isn't, then it becomes 1-0 * 200 * dt
	# simulation: if S is down, and W isn't, then it becomes 0-1 * 200 * dt
	# simulation: if both are down then it becomes 1-1 * 200 * dt
	# same with a and d

	# not the best, but we work with what we know
	if player.distance_to(coin) < 40:
		coin.x = random.randint(200,win.get_width()-200)
		coin.y = random.randint(200,win.get_height()-200)
		points+=1


def main(dt: float):
	move(dt)
	zcore.draw.clearBackground(win,"black")
	win.blit(background, (0,0))
	zcore.draw.fillCircle(win, "blue", coin,10)
	zcore.draw.fillRect(win, int(player.x),int(player.y), 20,20,"red")
	drawText(win, f"{points = }", 20,20,20,"red")
	drawText(win, f"{player.distance_to(coin)=}", 20,60,20,"red")

zcore.window.mainLoop(main)
