# For full list of keyboard commands, please refer to: #
# https://pythonhosted.org/pynput/keyboard.html#pynput.keyboard.Key #

# All the keys are coded based on my own key bindings. 
# Kindly change it accordingly based on your own preferences.
# To view the full list of my key bindings, please refer to KeyBindings.png

from pyautogui import press
import time

def keyPress(keyValue):
	press(keyValue)
	print ("'" + keyValue + "'" + " key pressed!")
	
	# To prevent keyboard input delay:
	time.sleep(0.5)
