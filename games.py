import random
import sys
import csv
from datetime import datetime
import os

list_b = list(range(1, 12))
list_r = list(range(0, 37))
even_chances = ["odd", "even", "black", "red", "1-18", "19-36", "1", "2", "3", "4", "5", "6", "1.", "2.", "3.", "4.", "5.", "6."]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
wheel = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
dice = list(range(1, 7))  

brain_user = []
brain_comp = []

def usernamer():
    try:
        username = ""
        while username in ["", " "]:
            username = input("What's your name? ").lower().replace(" ", "")
        return username
    except (EOFError, KeyboardInterrupt):
        sys.exit("\n\nProgram stopped.\n")

def main():
    global username
    username = name
    try:
        while True:
            decision = input("\nDo you want to play games, see the game instructions or get a player summary chart? \n(Games/Ins/Chart): ").lower().replace(" ", "")
            if decision == "games": 
                game = input("\nChoose one of the following games:\n1. Black Jack\n2. Roulette\n3. Street Dice\n").lower().replace(" ", "")
                if game in ("blackjack", "1", "1.", "bj"):
                    return black_jack(username, "black_jack")
                elif game in ("roulette", "2", "2.", "r"):
                    return roulette(username, "roulette")
                elif game in ("streetdice", "3", "3.", "sd"):
                    return street_dice(username, "street_dice")
            elif decision == "ins":
                ins = input("\nFor which game do you want to see the instructions? \n(Black Jack/Roulette/Street Dice): ").lower().replace(" ", "")
                if ins in ("blackjack", "black jack", "1", "1.", "bj"): ins_black_jack()
                elif ins in ("roulette", "2", "2.", "r"): ins_roulette()
                elif ins in ("streetdice", "street dice", "3", "3.", "sd"): ins_street_dice()
            elif decision == "chart": chart()
            else: print("\nInvalid input."); continue
    except (EOFError, KeyboardInterrupt):
        sys.exit("\n\nProgram stopped.\n")

def write(username, game, win, kind):
    folder = f"{os.getcwd()}/Highscores_{str(username).capitalize()}_Games/"
    name = f"highscore_{username}_{game}.csv"
    today = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    if os.path.isdir(folder) == False: os.mkdir(folder)
    file = f"{folder}/{name}"
    with open(file, "a+") as f:
        writer = csv.writer(f)
        if os.path.getsize(file) == 0:
            writer.writerow(["date", "win", "kind"])
        writer.writerow([today, win, kind])

def go(game=0, function=0):
    while True:
        inp = input("\nDo you want to stop, continue with this game or play a new game (or get instructions or a summary chart)?\n(Stop/Continue/New): ").lower().replace(" ", "")
        if inp == "stop": raise EOFError
        elif inp == "continue": function(username, game)
        elif inp == "new": main()
        else: print("\nInvalid input."); continue

def chart():
    today = datetime.now().strftime("%d-%m-%Y")
    n = 0
    folder = f"{os.getcwd()}/Chart_{username.capitalize()}_Games/"
    file = f"{folder}/chart_{username}_{today}.csv"
    if os.path.isdir(folder) == False: os.mkdir(folder)
    if os.path.exists(file): os.remove(file)
    for i in ["black_jack", "roulette", "street_dice"]:
        if os.path.exists(f"{os.getcwd()}/Highscores_{username.capitalize()}_Games/highscore_{username}_{i}.csv"):
            print(f"Existing data for {i.replace("_", " ").title()} ✅")
            with open(file, "a+") as charts:
                writer = csv.writer(charts)
                wins, losses, ties = 0, 0, 0
                while n != 1:
                    writer.writerow([f"Chart_{username.capitalize()}_Games on the {today}"]); writer.writerow([])
                    n += 1
                with open(f"{os.getcwd()}/Highscores_{username.capitalize()}_Games/highscore_{username}_{i}.csv", "r+") as game:
                    reader = csv.DictReader(game)
                    for row in reader:
                        win = row["win"].strip()
                        if win in ("Win!", "Jackpot!"): wins += 1
                        elif "No win." == win: losses += 1
                        else: ties += 1
                writer.writerow([i.replace("_", " ").title()])
                writer.writerow(["wins", "losses", "ties"]); writer.writerow([wins, losses, ties])
                writer.writerow([])
        else: 
            print(f"No data for {i.capitalize()} ❌")
            continue


def over(s, name, game, card):
    if name == "user_sum":
        win = "No win."
        kind = "Player's bust"
        message = f"You lost because your cards add up to {s}."
    else:
        win = "Win!"
        kind = "Competitor's bust"
        message = f"You won because your competitor's cards add up to {s}."

    if name == "user_sum":
        print(f"\nThis is your card: \033[35m{card}\033[0m.")

    colour = "\033[92m" if win == "Win!" else "\033[91m"
    print(f"\n{colour}{win} {message}\033[0m")
    write(username, "black_jack", win, kind)

def exact(s, name, game, card):
    if name == "user_sum":
        win = "Win!"
        kind = "Black Jack"
        message = "You won because your cards add up to exactly 21."
    else:
        win = "No win."
        kind = "Competitor's Black Jack"
        message = "You lost because your competitor's cards add up to exactly 21."

    if name == "user_sum":
        print(f"\nThis is your card: \033[35m{card}\033[0m.")

    colour = "\033[92m" if win == "Win!" else "\033[91m"
    print(f"\n{colour}{win} {message}\033[0m")
    write(username, "black_jack", win, kind)

def black_jack(username=0, game=0):
    global card
    brain_user.clear(); brain_comp.clear()

    print("")
    user = ""
    while user != "hold":
        card = random.choice(list_b)
        brain_user.append(card)
        user_sum = int(sum(brain_user))
        if user_sum > 21:
            over(user_sum, "user_sum", game, card); break
        elif user_sum == 21:
            exact(user_sum, "user_sum", game, card); break
        else:
            while True:
                user = input(f"This is your card: \033[35m{card}\033[0m. Hold/Take: ").lower().replace(" ", "")
                if user in ["hold", "take"]: break
                else: print("Invalid input.")

        if user == "hold":
            print("")
            comp = ""
            while comp != "Hold":
                card = random.choice(list_b)
                brain_comp.append(card)
                comp_sum = int(sum(brain_comp))
                print(f"Competitor: \033[35m{card}\033[0m")
                if comp_sum > 21:
                    over(comp_sum, "comp_sum", game, card); break
                elif comp_sum == 21:
                    exact(comp_sum, "comp_sum", game, card); break

                if comp_sum <= 10: weight_hold, weight_take = 0, 100
                elif comp_sum > 10 and comp_sum <= 15: weight_hold, weight_take = 30, 70
                elif comp_sum > 15 and comp_sum <= 17: weight_hold, weight_take = 75, 25
                elif comp_sum > 17 and comp_sum <= 20: weight_hold, weight_take = 93, 7
                what = random.choices(["Hold", "Take"], weights=(weight_hold, weight_take))[0] #only return first element
                print(f"Competitor chooses: {what}")
                
                if what == "Hold":
                    total_u, total_c = sum(brain_user), sum(brain_comp)
                    print(f"\nYour total: \033[35m{total_u}\033[0m\nYour competitor's total: \033[35m{total_c}\033[0m")
                    if total_u > total_c:
                        win, kind = "Win!", "Higher sum"
                        print("\n\033[92mYou won!\033[0m")
                    elif total_u < total_c:
                        win, kind = "No win.", "Lower sum"
                        print("\n\033[91mYour competitor won.\033[0m")
                    else:
                        win, kind = "Tie", "Tie"
                        print("\nTie!")
                    write(username, "black_jack", win, kind)
                    break
                else: continue 
        elif user == "take": continue    
    go(game, black_jack)   

def ins_black_jack():
    text_b = [
        "\nInstructions:\n-------------", 
        "\n• The goal of the game is to have the biggest sum of the numbers on the cards, hereby the numbers range from 1-11", 
        "• If the sum is over 21, one loses instantly but if the sum is exactly 21, one wins instantly. If none of those cases happen though, the player with the bigger sum wins.", 
        "• A random card with a random number on it will be drawn and you will be requested to decide whether to \"hold\" or to \"take\".", 
        "• If you choose \"hold\" you're done and it's your competitor's turn but if you choose otherwise a random card will be drawn again and you will be requested to choose again between the two possible options given (\"Hold\"/”Take\").", 
        "• When it's your competitor's turn, they will do the exact same thing.", 
        "• The game ends when: \n1. One player's sum equals exactly 21\n2. One player's sum is over 21.\n3. When the last player chooses to \"Hold\"."
        "\nIf both players have the same sum, it's a tie."]
    for i in text_b:
        input(i)


def rwrite(game, name, username, win, number, kind):
    print(f"\033[91mThe number is: {number} => {win}\033[0m") if "no" in win or "No" in win else print(f"\033[92mThe number is: {number} => {win}\033[0m")
    file = write(username, "roulette", win, kind)
    return go(game, name)

def roulette(username=0, game=0):
    number = random.choice(list_r)
    while True:
        for i in wheel:
            if i == 0:
                print(f"\033[47m\033[1;32m{i}\033[0m", end=", ")
            elif i == wheel[-1]:
                print(f"\033[47m\033[1;30m{i}\033[0m")
                break
            elif i in red:
                print(f"\033[47m\033[1;31m{i}\033[0m", end=", ")
            elif i in black:
                print(f"\033[47m\033[1;30m{i}\033[0m", end=", ")
        which: str = input("\nWhat do you want to bet on? Choose one of the following: \n   Inside bets:\n      1. Single number \n      2. 2 adjacent numbers\n      3. Neighbour numbers, 3 \n   Outside bets:\n      4. Even chances (black/red), (odd/even), (1-18/19-36) \n   - Note: If the number is zero, all outside bets automatically lose!\n").lower().replace(" ", "")
        if which == "singlenumber" or which == "1" or which == "1.":
            kind = "Single number"
            user = None
            while user not in list_r:
                try:
                    user = int(input(f"\nWhich number do you want to bet on: ").replace(" ", ""))
                    if user not in list_r:
                        raise ValueError
                except ValueError:
                    print("\nInvalid input"); continue
                break
            win = "Jackpot!" if number == user else "No win."
            rwrite(game, roulette, username, win, number, kind)
        elif which == "2adjacentnumbers" or which == "2" or which == "2.":
            kind = "2 adjacent numbers" 
            while True:
                try:
                    user = input(f"\nOn which 2 adjacent numbers do you want to bet one (x1, x2): ").replace(" ", "")
                    x1, x2 = user.split(","); x1, x2 = int(x1), int(x2)
                    if x1 not in list_r or x2 not in list_r:
                        raise ValueError
                    
                except ValueError:
                    print("Invalid input."); continue
                try:
                    if int(wheel.index(x1) + 1) == int(wheel.index(x2)) or int(wheel.index(x1) - 1) == int(wheel.index(x2)) or x1 == 0 and x2 == 26 or x1 == 26 and x2 == 0:
                        win = "Win!" if number == x1 or number == x2 else "No win."
                        rwrite(game, roulette, username, win, number, kind)
                    else:
                        raise ValueError
                except ValueError:
                    print("These are not numbers that can be used in this constellation."); continue
                break
        elif which == "neighbournumbers" or which == "3" or which == "3.":
            kind = "Neighbour numbers"
            while True:
                try:
                    x1 = int(input(f"\nOn which number and its neighbours do you want to bet on? Just input the middle number: ").replace(" ", ""))
                    if x1 not in list_r:
                        raise ValueError
                except ValueError:
                    continue
                idx = wheel.index(x1)

                x2 = wheel[(idx + 1) % len(wheel)]
                x3 = wheel[(idx - 1) % len(wheel)]
                
                win = "Win!" if number == x1 or number == x2 or number == x3 else "No win."
                rwrite(game, roulette, username, win, number, kind)
                break
        elif which == "evenchances" or which == "4" or which == "4.":
            user = None
            while user not in even_chances:
                user = input(f"\nDo you want to bet on:\n1. Even\n2. Odd\n3. Red\n4. Black\n5. 1-18\n6. 19-36\n").lower()
            if number == 0:
                win, kind = ("No win.", "Even chances: Zero")
                rwrite(game, roulette, username, win, number, kind)
            if user in ("1", "1.", "even"): win, kind = (("Win!" if number % 2 == 0 else "No win."), "Even chances: Even") 
            elif user in ("2", "2.", "odd"): win, kind = (("Win!" if number % 2 != 0 else "No win."), "Even chances: Odd")
            elif user in ("3", "3.", "red"): win, kind = (("Win!" if number in red else "No win."), "Even chances: Red")
            elif user in ("4", "4.", "black"): win, kind = (("Win!" if number in black else "No win."), "Even chances: Black")
            elif user in ("5", "5.", "1-18"): win, kind = (("Win!" if number in range(1, 19) else "No win."), "Even chances: 1-18")
            elif user in ("6", "6.", "19-36"): win, kind = (("Win!" if number in range(19, 37) else "No win."), "Even chances: 19-36")            
            rwrite(game, roulette, username, win, number, kind)
            break
        else:
            print("Invalid input.")
            continue

def ins_roulette():
    text_r = [
        "\nInstructions:\n-------------", 
        "\n• The goal of the game is to guess the random drawn number correctly, hereby the numbers range from 0-36", 
        "• You will be given 4 choices/bets (3 inside bets, 1 outside bet) you can take:", 
        "Inside bets:\n      1. Single number \n         You can input one number that you think will be drawn.\n      2. 2 adjacent numbers\n         You can input 2 adjacent numbers (2 numbers that are next to each other). If one of those two numbers are drawn, you win.\n      3. Neighbour numbers, 3 \n          You can input one number. If either that number or one of its two neighbours are drawn, you win.\n   Outside bets:\n      4. Even chances (black/red), (odd/even), (1-18/19-36)\n         You have to choose one of these 6 outcomes. If the number fulfills this exact outcome/criteria — black, red, odd, even, 1–18, or 19–36 — you win.\n   - Note: If the number is zero, all outside bets automatically lose!"]
    for i in text_r:
        input(i)

def sdwrite(username, game, win, kind, text):
    print(f"\033[92m{win} {text}\033[0m") if win == "Win!" else print(f"\033[91m{win} {text}\033[0m")
    write(username, game, win, kind)
    go(game, street_dice)

def street_dice(username=0, game=0):
    while True:
        user1, user2 = random.choice(dice), random.choice(dice)
        comp1, comp2 = random.choice(dice), random.choice(dice)

        user_total = user1 + user2
        comp_total = comp1 + comp2

        print(f"\nYour dice: {user1} + {user2} = {user_total}")
        print(f"Your competitor's dice: {comp1} + {comp2} = {comp_total}")

        if user_total != comp_total:
            break
        print("Tie! Reroll!\n")

    if user_total > comp_total:
        user1, user2 = random.choice(dice), random.choice(dice)
        roll_total = user1 + user2

        print("You're the shooter, so you get to dice!\n")
        print(f"Your dice: {user1} + {user2} = {roll_total}")

        if roll_total in [7, 11]:
            sdwrite(username, game, "Win!", "Natural", f"You won because you got a Natural, the \"{roll_total}\".")

        elif roll_total in [2, 3, 12]:
            sdwrite(username, game, "No win.", "Craps", f"You lost because you got Craps, the \"{roll_total}\".")

        else:
            point = roll_total
            user1, user2 = 0, 0
            print(f"Your point: {point}")

            while sum([user1, user2]) != 7 and sum([user1, user2]) != point:
                user1, user2 = random.choice(dice), random.choice(dice)
                roll_total = user1 + user2
                print(f"Your dice: {user1} + {user2} = {roll_total}")

            if roll_total == 7:
                sdwrite(username, game, "No win.", "7-out", "You lost because you got a 7-out.")
            else:
                sdwrite(username, game, "Win!", "Point", f"You won because you made the point, the \"{roll_total}\".")

    elif user_total < comp_total:
        comp1, comp2 = random.choice(dice), random.choice(dice)
        roll_total = comp1 + comp2

        print("Your competitor's the shooter, so they get to dice!\n")
        print(f"Your competitor's dice: {comp1} + {comp2} = {roll_total}\n")

        if roll_total in [7, 11]:
            sdwrite(username, game, "No win.", "Competitor's Natural", f"You lost because your competitor got a Natural, the \"{roll_total}\".")

        elif roll_total in [2, 3, 12]:
            sdwrite(username, game, "Win!", "Competitor's Craps", f"You won because your competitor got Craps, the \"{roll_total}\".")

        else:
            point = roll_total
            comp1, comp2 = 0, 0
            print(f"Your competitor's point: {point}")

            while sum([comp1, comp2]) != 7 and sum([comp1, comp2]) != point:
                comp1, comp2 = random.choice(dice), random.choice(dice)
                roll_total = comp1 + comp2
                print(f"Your competitor's dice: {comp1} + {comp2} = {roll_total}")

            if roll_total == 7:
                sdwrite(username, game, "Win!", "Competitor's 7-out", "You won because your competitor got a 7-out.")
            else:
                sdwrite(username, game, "No win.", "Competitor's point", f"You lost because your competitor made the point, the \"{roll_total}\".")

def ins_street_dice():
    text_sd = [
        "\nInstructions:\n-------------", 
        "\n• Firstly, the dice are rolled and the player with the higher sum is the \"shooter\".\nIf there's a tie, reroll.", 
        "• The shooter if going to roll the dice. \nIf they get either a 7 or an 11 (a Natural), they win instantly.\nIf they get a 2, 3 or a 12 (Craps), they lose instantly.", 
        "• If none of those cases happen (a 4, 5, 6, 8, 9, 10 is rolled), the shooter rolls the dice again. The sum of the dice' numbers now becomes the \"point\".", 
        "• In the next round, the shooter rolls the dice again. \nIf they roll their \"point\", they win instantly. \nIf they roll a 7, they lose instantly. \nIf none of those cases happen, the shooter rerolls as long as it takes to roll a 7 or their point."]
    for i in text_sd:
        input(i)


if __name__ == "__main__":
    try:
        print("\nWelcome to \"Games\", where you can play multiple single-player-games! \nHave fun!")
        name = usernamer()
        main()
    except (EOFError, KeyboardInterrupt):
        sys.exit("\n\nProgram stopped.\n")
        




