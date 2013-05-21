# File: dragon.py
# Author Name: Dwight Dickinson
# Last Modified By: Dwight Dickinson
# Date Last Modified: May 19th 2013
# Revision History
# 1.0 - May 19th 2013
# 	- Added comments and header information
# 	- Removed the randomization
#	- Changed the print statements for the first decision
#	- Changed the method names

# 1.1 - May 20th 2013
#	- Added second decision level
#	- Added new functions for final decision level

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
	time.sleep(2)
	print ('It is dark and spooky...')
	time.sleep(2)
	print ('The exit behind you caves in and you must proceed forward...')
	
	print
	time.sleep(2)

	if chosenCave == '1':
		print('The cave branches off into two tunnels...')
		time.sleep(2)
		print('The left tunnel has a light illuminating from it, and the right has a voice yelling faintly saying HELP...')
		time.sleep(2)
		print
		print('Which tunnel will you choose? (Left, or Right)')
		decision = raw_input()
		cave1(decision)
	elif chosenCave == '2':
		print('The cave has two holes in the ground...')
		time.sleep(2)
		print('The left hole has a ladder for you to climb down, the right appears to be a slide')
		time.sleep(2)
		print
		print('Which hole will you proceed down? (Left, or right)')
		decision = raw_input()
		cave2(decision)

# These are the decision trees for the second decision
def cave1(chosenTunnel):
	decision = ''
	if chosenTunnel.upper() == 'LEFT':
		print
		print('You proceed down the left tunnel with caution...')
		time.sleep(2)
		print('The light becomes brighter...')
		time.sleep(2)
		print('A person carrying a torch appears from the corner with an evil looking smile on his face.')
		time.sleep(2)
		print
		print('Do you run away, or stay put? (run, or stay)')
		decision = raw_input()
		light(decision)
		
	elif chosenTunnel.upper() == 'RIGHT':
		print
		print('You proceed towards the voice...')
		time.sleep(2)
		print('The voice begins to get raspy...')
		time.sleep(2)
		print('The voice becomes a fierce roar as a dragon appears infront of you...')
		time.sleep(2)
		print('Do you run away, or try to fight the dragon. (run, or fight)')
		print
		decision = raw_input()
		fight(decision)
	
def cave2(chosenPath):
	print
	
	
#Light decisions
def light(runOrStay):
	if runOrStay.upper() == 'RUN':
		print('You run
	
def fight(runOrFight):
	
	
def main():
	
	
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		caveNumber = chooseCave()
		firstDecision(caveNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
