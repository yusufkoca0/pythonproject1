how to run: python3 main.py

sample i/o is in the sampleIO.zip file.

How to play the game:

First input describes the maze. it's an nxm sized maze with a max size 10x10.

W means wall, C means carrot, A means apple, M means meat, X means free space, P means poison, * is rabbit.

Second input is commands.

U is up, D is down, L is left, R is right.

if rabbit eats carrot its a +10 points, apple is +5 and meat is -5 points.
if rabbit eats the poison game is over.
if rabbit does not eat the poison, game ends when the all commands has been taken. And program displays a score.
