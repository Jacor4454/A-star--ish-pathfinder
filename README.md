# A-star(-ish) pathfinder
this is one of if not the first things I coded

## backstory
I started coding a few years ago for my A-level. I had almost no prior experience in coding and what I did have was scratch. After 2 weeks of background my teacher siad me and the other inexperienced students could code something called the "monster game" (a turn based dungeon crawler printed with letters in the terminal (see the "monter.py" file)) After a day I had the game and some levels coded (this was before I knew how to use files properly) and with the teacher wanting us to spend another week on it to get the basics I turned to making the opponent more advanced. That is how I developed the pathfinder and then the A-star pathfinder. I then took the pathfinder and put it in a grid generator to show how it works.

## the game
so the game itself is called the monster game but I called it grid code. all you do if press "w", "a", "s" and "d" to move your character (reprisented by the I but that will be in the key below). at any time you can type "save" to save your progress at that time. randomly across the room you will stumble over some traps (show by a message and your character displaying an "O") which will wake up the monster (the "K") (who uses the "a-star" pathfinder) and will start moving towards you every turn. the exits to the rooms are shown by the 2 lines sticking out the grid at the bottow or right side. there is also treasure "T" that will give you bonus points. If at any point you get attacked by the monster you will enter a turn based battle that I was developing when I stopped (so it isnt balanced at all but feel free to carry on the basics are there).

## key:

### objects:

    "I" - your character that you can move
    "K" - the monter (avoid)
    "W" - walls, you can't walk through
    "O" - traps that have been acivated
    "T" - treasure (gather for bonus points)
    "|" or "---" - grid spacers

### commands:

    "w" - move up
    "s" - move down
    "a" - move left
    "d" - move right
    "save" - save the game
