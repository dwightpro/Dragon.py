# File: dragon.py
# Author Name: Dwight Dickinson
# Last Modified By: Dwight Dickinson
# Date Last Modified: May 19th 2013
#
# Revision History
# 1.0 - May 19th 2013
# 	- Added comments and header information
# 	- Removed the randomization
#	- Changed the print statements for the first decision
#	- Changed the method names
#
# 1.1 - May 20th 2013
#	- Added second decision level
#	- Added new functions for final decision level
#
# 1.2 - May 21st 2013
#	- Added second cave decision path
#	- Added final end-game decision results
#
# 1.3 - May 21st 2013
#	- Removed unnecessary code
#	- Added cave 2 decision path
#	- Added final decision path

import time

def displayIntro():
	print ('You are on a planet full of dragons. In front of you,')
	print ('you see two caves. In one cave, the dragon is friendly')
	print ('and will share his treasure with you. The other dragon')
	print ('is greedy and hungry, and will eat you on sight.')
	print
	
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print ('Which cave will you go into? (1 or 2)')
		cave = raw_input()
	return cave

def firstDecision(chosenCave):
	decision = ''
	print ('You approach the cave...')
	time.sleep(1)
	print ('It is dark and spooky...')
	time.sleep(1)
	print ('The exit behind you caves in and you must proceed forward...')
	
	print
	time.sleep(1)

	if chosenCave == '1':
		print('The cave branches off into two tunnels...')
		time.sleep(1)
		print('The left tunnel has a light illuminating from it, and the right has a voice yelling faintly saying HELP...')
		time.sleep(1)
		print
		print('Which tunnel will you choose? (Left, or Right)')
		decision = raw_input()
		cave1(decision)
	elif chosenCave == '2':
		print('The cave has two holes in the ground...')
		time.sleep(1)
		print('The left hole has a ladder for you to climb down, the right appears to be a slide')
		time.sleep(1)
		print
		print('Which hole will you proceed down? (Left, or right)')
		decision = raw_input()
		cave2(decision)

# These are the decision trees for the second decision
def cave1(chosenTunnel):
	decision = ''
	print
	if chosenTunnel.upper() == 'LEFT':
		print('You proceed down the left tunnel with caution...')
		time.sleep(1)
		print('The light becomes brighter...')
		time.sleep(1)
		print('A person carrying a torch appears from the corner with an evil looking smile on his face.')
		time.sleep(1)
		print
		print('Do you run away, or stay put? (run, or stay)')
		decision = raw_input()
		light(decision)
		
	elif chosenTunnel.upper() == 'RIGHT':
		print('You proceed towards the voice...')
		time.sleep(1)
		print('The voice begins to get raspy...')
		time.sleep(1)
		print('The voice becomes a fierce roar as a dragon appears infront of you...')
		time.sleep(1)
		print('Do you run away, or try to fight the dragon. (run, or fight)')
		print
		decision = raw_input()
		fight(decision)
	
def cave2(chosenPath):
	decision = ''
	print
	if chosenPath.upper() == 'LEFT':
		print('You proceed to go down the hole carefully climbing down each step...')
		time.sleep(1)
		print('A step breaks and you fall...')
		time.sleep(1)
		print('You catch yourself on one of the ladder steps...')
		time.sleep(1)
		print
		print('Do you climb back up, or let go? (climb, or fall)')
		decision = raw_input()
		ladder(decision)
		
	elif chosenPath.upper() == 'RIGHT':
		print('You jump into the hole...')
		time.sleep(1)
		print('You begin to slide down until suddenly you hit the ground...')
		time.sleep(1)
		print('You can go up the stairs to the left, or down the tunnel straight ahead.')
		time.sleep(1)
		print('Where will you go? (stairs, or tunnel)')
		decision = raw_input()
		slide(decision)
	
	
#Light decisions
def light(runOrStay):
	if runOrStay.upper() == 'RUN':
		print('You run away from the person carrying the torch...')
		time.sleep(1)
		print('He yells out a weird demonic phrase...')
		time.sleep(1)
		print('The phrase summons a dragon who appears and swallows you whole.')
		
	elif runOrStay.upper() == 'STAY':
		print('You approach the person carrying the torch...')
		time.sleep(1)
		print('He disappears in a cloud of dust as you approach him...')
		time.sleep(1)
		print('A dragon appears from behind you and sets your body aflame.')
	
def fight(runOrFight):
	if runOrFight.upper() == 'RUN':
		print('You run in fear from the dragon...')
		time.sleep(1)
		print('You make it out of the tunnel only to fall in the hole you saw earlier.')
		time.sleep(1)
		print('You land right in another dragons mouth and are swallowed whole')
		
	elif runOrFight.upper() == 'FIGHT':
		print('You draw your swords and prepare for battle...')
		time.sleep(1)
		print('The dragon swipes his hand at you, knocking your swords out of your hands')
		time.sleep(1)
		print('You draw your bow and set the arrow aflame...')
		time.sleep(1)
		print('You shoot the arrow at the dragons head which ignites the whole body...')
		time.sleep(1)
		print
		print
		print('The dragon falls.... YOU WIN')
		
#Hole decisions
def ladder(climbOrFall):
	if climbOrFall.upper() == 'CLIMB':
		print('You try to climb back up...')
		time.sleep(1)
		print('Your hand slips and you begin to fall...')
		time.sleep(1)
		print('You fall into the mouth of the dragon and he swallows you whole.')
	elif climbOrFall.upper() == 'FALL':
		print('You let go of the ladder...')
		time.sleep(1)
		print('You fall into the mouth of the dragon that was waiting below.')
	
def slide(stairsOrTunnel):
	if stairsOrTunnel.upper() == 'TUNNEL':
		print('You walk straight through the tunnel when suddenly the roof trembles...')
		time.sleep(1)
		print('The roof caves in ontop of you...')
		time.sleep(1)
		print('As you take your last breath of air, you see a dragon that ignites the cavern')
		
	elif stairsOrTunnel.upper() == 'STAIRS':
		print('You begin to walk up the stairs carefully...')
		time.sleep(1)
		print('You notice the steps begin to crack...')
		time.sleep(1)
		print('Without warning, the stairs explode and leak lava, killing you instantly.') 
		
def main():
	
	
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		caveNumber = chooseCave()
		firstDecision(caveNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
