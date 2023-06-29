import os
import random
import time

# Game settings
width = 50
height = 20
player = "V(^w^)V"
enemy = "X"
bullet = "|"
enemy_speed = 4
sleep_time = 0.1

# Initialize player position
player_x = width // 2
player_y = height - 1

# Initialize enemy position
enemy_x = random.randint(0, width - 1)
enemy_y = 0

# Initialize bullet position
bullet_x = player_x
bullet_y = player_y

# Track time elapsed for enemy movement
time_elapsed = 0

# Game loop
while True:
	# Clear the screen
	os.system("cls" if os.name == "nt" else "clear")

	# Draw the game board
	for y in range(height):
		for x in range(width):
			if y == player_y and x == player_x:
				print(player, end="")
			elif y == enemy_y and x == enemy_x:
				print(enemy, end="")
			elif y == bullet_y and x == bullet_x:
				print(bullet, end="")
			else:
				print(" ", end="")
		print()

	# Move enemy down
	if time_elapsed % enemy_speed == 0:
		enemy_y += 1

	# Move bullet up
	bullet_y -= 1

	# Check collision
	if bullet_y == enemy_y and bullet_x == enemy_x:
		# Enemy destroyed
		enemy_x = random.randint(0, width - 1)
		enemy_y = 0
		bullet_x = player_x
		bullet_y = player_y

	# Check if the enemy reached the player
	if enemy_y == player_y:
		print("Game Over!")
		break

	# Update the game
	time.sleep(sleep_time)
	time_elapsed += 1

	# Get user input
	if os.name == "nt":
		import msvcrt

		if msvcrt.kbhit():
			key = msvcrt.getch().decode()
			if key == "a" and player_x > 0:
				player_x -= 1
			elif key == "d" and player_x < width - 1:
				player_x += 1
			elif key == "w":
				bullet_x = player_x
				bullet_y = player_y

	else:
		import sys
		import termios
		import tty

		def getkey():
			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)

			try:
				tty.setraw(sys.stdin.fileno())
				ch = sys.stdin.read(1)
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

			return ch

		key = getkey()
		if key == "a" and player_x > 0:
			player_x -= 1
		elif key == "d" and player_x < width - 1:
			player_x += 1
		elif key == "w":
			bullet_x = player_x
			bullet_y = player_y
