from pygame.math import Vector2
# screen
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 708
TILE_SIZE = 64

#traits
TRAIT = {
	0 : 'SILVER BULLET: + 25% bullet speed',
	1 : 'THE MORE THE MERRIER: Give additional bullet.',
	2 : 'DOUBLE TROUBLE: x2 Resistance',
	3 : 'SPEEDO: + 50% speed run',
	4 : 'RICH: - 50% cooldown bullet',
	5 : 'KHE UOC QUY DU: -50% HP but x3 bullet & + 25% speed run'
}


# overlay positions 
OVERLAY_POSITIONS = {
	'tool' : (40, SCREEN_HEIGHT - 15), 
	'seed': (70, SCREEN_HEIGHT - 5)}

PLAYER_TOOL_OFFSET = {
	'left': Vector2(-50,40),
	'right': Vector2(50,40),
	'up': Vector2(0,-10),
	'down': Vector2(0,50)
}

LAYERS = {
	'water': 0,
	'ground': 1,
	'soil': 2,
	'soil water': 3,
	'rain floor': 4,
	'house bottom': 5,
	'ground plant': 6,
	'main': 7,
	'house top': 8,
	'fruit': 9,
	'rain drops': 10
}

APPLE_POS = {
	'Small': [(18,17), (30,37), (12,50), (30,45), (20,30), (30,10)],
	'Large': [(30,24), (60,65), (50,50), (16,40),(45,50), (42,70)]
}

GROW_SPEED = {
	'corn': 1,
	'tomato': 0.7
}

SALE_PRICES = {
	'wood': 4,
	'apple': 2,
	'corn': 10,
	'tomato': 20
}
PURCHASE_PRICES = {
	'corn': 4,
	'tomato': 5
}
