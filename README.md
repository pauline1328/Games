# Games
#### **<ins>Description:<ins>**

This project consists of 3 files:
- games.py
- requirements.txt
- README.md

The program is a game called **"Games"** which contains 3 single-player games:
- Black Jack
- Roulette
- Street Dice

After a game has been completed at least once, player progress and wins/losses as well as their kind are automatically stored in CSV files for the corresponding game and user.

---

#### **<ins>Usage:<ins>**

`python games.py`

This program is an "Interactive console program" and functions through input().

The whole program can be stopped at any time by pressing `Ctrl + C` or `Ctrl + D`.  

After starting the game, one is asked for a username, and should then decide between playing a game, viewing the personal user chart or stopping the program entirely.

### **<ins>Features:<ins>**
- 3 single-player games:
   - Black Jack
   - Roulette
   - Street Dice
- Automatic player results tracking: game wins/losses and their kind per player
- Optional instructions for each game
- Personalized player summary charts

### **<ins>Functioning:<ins>**

In games.py there are 15 functions, including the `main()` function.

The script starts off by importing different libraries, listed in the requirements.txt file.

A few lists follow such as the lists of red and black numbers on the roulette wheel, the chronological order of numbers on the wheel and the list of numbers on the die.    

---

As the program starts, a welcome message is printed, and the `usernamer()` as well as the `main()` function are called through the main guard.

The first function is `usernamer()` which fulfills the purpose of asking the user for a username that is required for identifying the user and linking them to their correct high score and chart files. 

The `main()` function determines whether the user wants to play games or get a personalized user chart which shows a summary of their number of wins and losses in all games played so far.  
If the user chooses to play games though, they have three options to choose from - listed above.

The `dec()` function is called earlier in `main()` where the user decides whether they want to see instructions for certain games.

The `write()` function is responsible for writing the CSV files, distributing the right information per user and game.  

<br>

The `go()` function is called after every game ends; the user can decide whether they want to keep playing the same game, play a new game, get a personalized user chart CSV file or if they want to stop the whole program.

The next function `chart()` creates the personalized chart CSV file in which all the wins, losses and ties of the user are registered for each game.


#### **<ins>Black Jack</ins>**
The next two functions, `over()` and `exact()`, are essential for the first game, Black Jack.   
If the total of the drawn cards exceeds 21, `over()` is called, the win/loss statement is printed, and the `write()` function records the result. For the `exact()` function to be called, the total has to add up to exactly 21.

The function `black_jack()` is the main function for this game. It works as follows: a card for the user will be drawn with a random number on it. The user can type in "Hold" and the next card is drawn. If the user_sum == 21: `exact()` if the user_sum > 21: `over()`. If none of those cases happen, it will go on like that until the user types in "Hold" instead of "Take".  
After that the computer will play its turn. The winner is the one with the higher sum, or the one whose sum equals exactly 21.  
After the game ends, the `go()` function is called. 

The `ins_black_jack()` function prints out the Roulette instructions, if needed.

#### **<ins>Roulette</ins>**
The `rwrite()` function prints out the user’s win/loss result in the Roulette game and calls the `write()` function to save it in the CSV file.   
After that, the `go()` function is called.

The `roulette()` function is the main function for the game. 
At first, the roulette \"wheel\" is printed out where each number is either red or black (or green if it's 0) so that it's easier to place the following bet.
The user has 4 betting options: 
- Single number bet: Bet on one number
- 2 adjacent numbers: 2 adjacent numbers on the European roulette wheel
- Neighbour numbers: 1 number and its two neighbours on the European roulette wheel
- Even chances bet: Even, Odd, Red, Black, 1-18, 19-36 number

A random number will be drawn by the program and if it fits the criteria the user picked, the user wins.

The `ins_roulette()` function prints out the Roulette instructions, if needed.

#### **<ins>Street Dice</ins>**
The `sdwrite()` function basically serves the same purpose as the `rwrite()` function; it prints out the win/loss message and calls `write()`.

The game Street Dice is executed with the function `street_dice()`. The user's and the computer's dice are rolled using the random library.   
The higher roll becomes the shooter, sets the bet and rolls again.   
A 7 or 11 means a win, while 2, 3, or 12 means a loss and any other value becomes the point.  
If there's a point, the shooter continues rolling until either a 7 or their point is rolled — at which point the win or loss is determined.  
If there's a tie, the game will just "reroll".

The `ins_street_dice()` function prints out the instructions for Street Dice if needed.

---
### **<ins>Detailed Game Instructions:<ins>**

<details closed>
<summary><ins>Instructions Black Jack:</summary>

The goal of the game is to have the biggest sum of the numbers on the cards, hereby the numbers range from 1-11
- If the sum is over 21, one loses instantly but if the sum is exactly 21, one wins instantly.      
If none of those cases happen though, the player with the bigger sum wins.
- A random card with a random number on it will be drawn and you will be requested to decide whether to \"hold\" or to \"take\".
- If you choose \"hold\" you're done and it's your competitor's turn but if you choose otherwise a random card will be drawn again and you will be requested to choose again between the two possible options given (\"Hold\"/”Take\").
- When it's your competitor's turn, they will do the exact same thing.
- The game ends when: 
   1. One player's sum equals exactly 21
   2. One player's sum is over 21.
   3. When the last player chooses to \"Hold\"

</details>

<details closed>
<summary><ins>Instructions Roulette:</summary>

The goal of the game is to guess the random drawn number correctly, hereby the numbers range from 0-36.  
You will be given 4 choices/bets (3 inside bets, 1 outside bet) you can take:  
1. Single number 
You can input one number that you think will be drawn.
2. 2 adjacent numbers
You can input 2 adjacent numbers (2 numbers that are next to each other). If one of those two numbers are drawn, you win.
3. Neighbour numbers, 3 
You can input one number. If either that number or one of its two neighbours are drawn, you win.
4. Even chances (black/red), (odd/even), (1-18/19-36)
You have to choose one of these 6 outcomes. If the number fulfills this exact outcome/criteria — black, red, odd, even, 1–18, or 19–36 — you win.
- Note: If the number is zero, all outside bets automatically lose!  

</details>

<details closed>
<summary><ins>Instructions Street Dice:</summary>

- Firstly, the dice are rolled and the player with the higher sum is the \"shooter\".     
If there's a tie, reroll.
- The shooter is going to roll the dice.    
   - If they get either a 7 or an 11 (a Natural), they win instantly.
   - If they get a 2, 3 or a 12 (Craps), they lose instantly.  
   - If none of those cases happen (a 4, 5, 6, 8, 9, 10 is rolled), the shooter rolls the dice again. 
      - The sum of the dice' numbers now becomes the \"point\".
      - In the next round, the shooter rolls the dice again. 
      - If they roll their \"point\", they win instantly.
      - If they roll a 7, they lose instantly. 
      - If none of those cases happen, the shooter rerolls as long as it takes to roll a 7 or their point.
</details>
