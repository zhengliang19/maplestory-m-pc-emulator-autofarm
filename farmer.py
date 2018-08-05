#################     To Do List    #####################
#                                                       #
# 1. Auto Join PT                                       #
# 2. Auto Change Channel                                #
# 3. Auto Join Dungeon                                  #
# 4. Properly define the list of keys                   #
# 5. Solve key conflict issues when casting buff + skill#
# 6. ???                                                #
#                                                       #
#########################################################

from keypress import keyPress
import time
import threading
import random

directions = 1
noOfSkillsSet = 1 # The number of set of skills your character has. 

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

# Modify this accordingly based on your skill key bindings
def buffCast():
	# Cast buffs every N mins
	# This is to prevent consistent behaviours on your player which might trigger the BOT detectors.
	global noOfSkillsSet
	rand = random.sample(range(2994, 3650), 50)
	threading.Timer(random.choice(rand), buffCast).start()
	buffKeys = ['1', '2', '3', '4']
	switchKey = 'f1'
	for x in range(noOfSkillsSet): # 3 Sets of skill key bindings
		for keyValue in buffKeys:
			keyPress(keyValue)
		if (noOfSkillsSet != 1):
			keyPress(switchKey)
			
	
	
	
