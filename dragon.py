' File: dragon.py
' Author Name: Dwight Dickinson
' Last Modified By: Dwight Dickinson
' Date Last Modified: May 19th 2013
' Revision History
' 1.0 - May 19th 2013
' 	- Added comments and header information
' 	- Removed the randomization
'	- Changed the print statements for the first decision
'	- Changed the method names

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
	elif chosenCave == '2'
		print('The cave has two holes in the ground...')
		time.sleep(2)
		print('The left hole has a ladder for you to climb down, the right appears to be a slide')
		time.sleep(2)
		print
		print('Which hole will you proceed down?')
		decision = raw_input()
		cave2(decision)

' These are the decision trees for the second decision
def cave1(chosenTunnel):
	print('The ')
	
def cave2(chosenPath):
	print('The ')
	
	
def main():
	
	
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		caveNumber = chooseCave()
		firstDecision(caveNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
