#################     To Do List    #####################
#                                                       #
# 1. Auto Join PT                                       #
# 2. Auto Change Channel                                #
# 3. Auto Join Dungeon                                  #
# 4. Properly define the list of keys                   #
# 5. ???                                                #
#                                                       #
#########################################################

# For full list of keyboard commands, please refer to: #
# https://pythonhosted.org/pynput/keyboard.html#pynput.keyboard.Key #

# All the keys are coded based on my own key bindings. 
# Kindly change it accordingly based on your own preferences.
# To view the full list of my key bindings, please refer to KeyBindings.png


from pyautogui import press
import time
import threading
import random

directions = 1

def keyPress(keyValue):
	press(keyValue)
	print ("'" + keyValue + "'" + " key pressed!")
	
	# To prevent keyboard input delay:
	time.sleep(0.5)
	
def skillCast():
	global directions
	rand = [1, 2, 3, 4, 5]	
	# Cast your main skill for N times 
	# This is to prevent consistent behaviours on your player which might trigger the BOT detectors.
	for x in range(random.choice(rand)):
		keyPress('q')
		time.sleep(0.5)
	# Press direction key twice to change direction
	if directions:
		keyPress('d') #keyPress('right')
		keyPress('d') #keyPress('right')
	else:
		keyPress('a') #keyPress('left')
		keyPress('a') #keyPress('left')
	directions = not directions
	
print ("Program Started.")
print ("Press Ctrl + C to exit.")
while True:
	skillCast()
	
	
	