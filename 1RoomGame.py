intro = 'Welcome to 1Room! You awake in an dungeon cell with nothing but your dagger and wits. Use "E" "W" "S" and "N" when prompted.\n'
print(intro)

playerName = input('who are you?\n')
print(playerName)

if playerName:
    print('Welcome ' + playerName + ' are you awake?\n')

answerOne = input()
if answerOne == 'yes' or 'y':
    print('The floor is cold and grimey. In your mouth is the strong taste of iron.\n')
else:
    print('You toss and turn, switching in-between nightmares of carnage and paradise.\n')

seqOne = 'You wake up in a dark room, confused with an throbbing pain in your head. Where do you look first?\n'
print(seqOne)

choiceOne = input()
if choiceOne == 'e':
    print('On the dungeon walls are rusty shackles and pieces of skeletons. You are not the first one to be stuck here.\n')
elif choiceOne == 'w':
    print('Deeper within the cell, you hear the gnawling of bones. There is something here with you.\n')
elif choiceOne == 'n':
    print('The ceiling is stone, you think. Whatever it is, not even moonlight can penetrate it.\n')
elif choiceOne == 's':
    print('Are you above ground? or below it? That"s unknown to you.\n')
else:
    print('You check your person. You are free. Whoever captured you didn"t take your dagger.\n')

seqTwo = 'Regardless, you"re stuck. Do you take a step forward or stay put?\n'
print(seqTwo)

answerTwo = input()
if answerTwo == 'step forward' or 'step':
    print('Just as you take your first step, the creature in the dark pounces at you.\n')
else:
    print('You dont even have the chance to compose your thoughts when an creature lunges at you from the dark.\n')

import random 
die1 = random.randint(1, 20)
print(die1)

from time import sleep
sleep(2)

if die1 == 20:
    print('Swiftly, the dagger is through the goblins neck and it dies. You are safe, for now.\n')
if die1 == 2 or 19:
    print('You struggle, but the goblin is stronger, and after a few minutes, it bites your neck.\n')
if die1 == 1:
    print('The goblin bites your neck, killing you instantly')

from time import sleep
sleep(3)

gameOver = 'Thank you so much for playing! Reload if you wish to play again!'
print(gameOver)
