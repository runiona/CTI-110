#!/usr/bin/env python3
# Number Guessing Game with betting, a shop and a bankruptcy penalty.
#
# Quick guide to reading this file:
#   - "#" starts a comment: a note for humans that Python ignores.
#   - A "def" block is a function: a named chunk of code we can reuse.
#   - f"text {variable}" is an f-string: {} inserts a value into the text.
#
# How the game works:
#   1. Pick a difficulty and a bet. Guess the number to win money.
#   2. Out of guesses (or quit) = you lose your bet.
#   3. Spend money in the shop on power-ups.
#   4. Can't afford the minimum bet? You're bankrupt: type 50 random numbers
#      perfectly to get a bailout. One typo and you start over!
#
# Run it with:  python3 number_guesser.py
 
f"""Number Guessing Game with difficulty levels, math hints, betting and a shop."""
 
import math    # math tools (square roots)
import random  # random numbers and shuffling
 
# ----------------------------------------------------------------------------
# SETTINGS (ALL_CAPS names are constants: set once, never changed)
# ----------------------------------------------------------------------------
# A dictionary stores key: value pairs. Each value here is a tuple (a fixed
# group): (lowest number, highest number, guesses allowed, hints allowed)
DIFFICULTIES = {
    f"easy":   (1, 10, 5, 3),
    f"normal": (1, 50, 7, 3),
    f"hard":   (1, 100, 8, 4),
    f"insane": (1, 500, 10, 5),
}
 
# Secret mode: same layout, but not in the menu. Rare chance in insane mode.
BONUS_MODE = (1, 10000, 14, 6)
BONUS_CHANCE = 1 / 200  # 1 in 200 (0.5%)
 
# Betting settings
STARTING_MONEY = 500
BAILOUT_MONEY = 100   # money you get after the bankruptcy penalty
MIN_BET = 10          # also the "bankrupt" line
TYPING_COUNT = 50     # numbers to type when bankrupt
 
# Winnings = bet x multiplier (0.5 means half your bet)
PAYOUT_MULTIPLIERS = {
    f"easy":   0.5,
    f"normal": 1.0,
    f"hard":   1.5,
    f"insane": 3.0,
}
BONUS_MULTIPLIER = 8.0
SPEED_BONUS_RATE = 0.05   # +5% of bet per unused guess
HINT_PENALTY_RATE = 0.10  # -10% of bet per hint used
 
# Shop items. "when" is either "round" (use during a round) or "before"
# (switch on before a round starts).
SHOP_ITEMS = {
    f"extra_guess": {
        f"name": f"Extra Guess", f"price": 60, f"when": f"round",
        f"desc": f"Use during a round: adds 1 guess.",
    },
    f"bonus_hints": {
        f"name": f"Bonus Hints", f"price": 40, f"when": f"round",
        f"desc": f"Use during a round: adds 2 more hints.",
    },
    f"range_finder": {
        f"name": f"Range Finder", f"price": 100, f"when": f"round",
        f"desc": f"Use during a round: shows a window the number is inside.",
    },
    f"double_down": {
        f"name": f"Double Down", f"price": 80, f"when": f"before",
        f"desc": f"Before a round: winnings x2, but a loss costs 2x your bet.",
    },
    f"safety_net": {
        f"name": f"Safety Net", f"price": 90, f"when": f"before",
        f"desc": f"Before a round: if you lose, half of your loss is refunded.",
    },
}
 
# List comprehension: a one-line loop that builds a list.
# This reads: "every key whose item has when == round".
ROUND_ITEMS = [key for key, item in SHOP_ITEMS.items() if item[f"when"] == f"round"]
PRE_ROUND_ITEMS = [key for key, item in SHOP_ITEMS.items() if item[f"when"] == f"before"]
 
 
# ----------------------------------------------------------------------------
# THE PLAYER
# ----------------------------------------------------------------------------
# Everything about the player lives in one dictionary. Functions that receive
# it change the SAME dictionary, so updates (like money) stick.
def new_player():
    return {
        f"money": STARTING_MONEY,
        # Dictionary comprehension: {"extra_guess": 0, "bonus_hints": 0, ...}
        f"inventory": {key: 0 for key in SHOP_ITEMS},
    }
 
 
def show_wallet(player):
    money = player[f"money"]
    print(f"\nWallet: ${money:,}")  # :, adds commas (1,000)
    owned = [
        f"{SHOP_ITEMS[key][f'name']} x{count}"
        for key, count in player[f"inventory"].items()
        if count > 0
    ]
    # "A or B" gives B when A is empty
    print(f"Power-ups: {', '.join(owned) or f'none'}")
 
 
# ----------------------------------------------------------------------------
# MATH HELPERS FOR HINTS
# ----------------------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False  # "return" sends an answer back
    # % is the remainder after dividing (10 % 3 = 1). Remainder 0 = divides evenly.
    for i in range(2, math.isqrt(n) + 1):  # isqrt = whole-number square root
        if n % i == 0:
            return False
    return True
 
 
def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n  # ** means "to the power of"
 
 
def build_hints(secret, low, high):
    """Return a shuffled list of math hints about the secret number."""
    hints = []  # a list; .append() adds an item to the end
 
    # "A if condition else B" picks A or B
    parity = f"even" if secret % 2 == 0 else f"odd"
    hints.append(f"The number is {parity}.")
 
    for d in (3, 4, 5, 7):
        if d <= high:
            negation = f"" if secret % d == 0 else f"NOT "
            hints.append(f"The number is {negation}divisible by {d}.")
 
    if high >= 4:
        if is_prime(secret):
            hints.append(f"The number is prime.")
        elif secret > 1:  # "elif" = else if
            hints.append(f"The number is composite (not prime).")
 
    if is_perfect_square(secret):
        hints.append(f"The number is a perfect square.")
    elif high >= 10:
        root = math.isqrt(secret)
        hints.append(f"The square root of the number is between {root} and {root + 1}.")
 
    if high >= 10:
        # Turn the number into text, loop over each digit, and add them up.
        digit_sum = sum(int(c) for c in f"{secret}")
        hints.append(f"The digits of the number add up to {digit_sum}.")
        hints.append(f"The number has {len(f'{secret}')} digit(s).")
 
    mid = (low + high) // 2  # // divides and drops the decimal (7 // 2 = 3)
    hints.append(
        f"The number is greater than {mid}." if secret > mid
        else f"The number is {mid} or less."
    )
 
    if high >= 10:
        hints.append(f"The remainder when the number is divided by 10 is {secret % 10}.")
 
    random.shuffle(hints)  # random order every game
    return hints
 
 
def find_range_window(secret, low, high):
    """Range Finder power-up: a window of numbers that contains the secret."""
    size = max(3, (high - low + 1) // 5)  # about 1/5 of the range, at least 3
    # Choose a start so the window includes the secret and stays in range.
    earliest = max(low, secret - size + 1)
    latest = min(secret, high - size + 1)
    start = random.randint(earliest, latest)
    return start, start + size - 1  # a function can return two values
 
 
# ----------------------------------------------------------------------------
# MENUS
# ----------------------------------------------------------------------------
def choose_difficulty():
    print(f"\nChoose a difficulty:")
    # Loop over key AND value; the tuple is unpacked into four names.
    for name, (lo, hi, guesses, hints) in DIFFICULTIES.items():
        pays = PAYOUT_MULTIPLIERS[name]
        # {name:<7} pads to 7 characters; {pays:g} drops extra zeros (1.0 -> 1)
        print(f"  {name:<7} range {lo}-{hi}, {guesses} guesses, {hints} hints, pays {pays:g}x")
 
    while True:  # repeat until we return a valid answer
        # input() returns what the player typed; .strip() removes spaces,
        # .lower() makes it lowercase.
        choice = input(f"> ").strip().lower()
        if choice in DIFFICULTIES:  # "in" checks a dictionary's keys
            return choice
        print(f"Please type one of: {', '.join(DIFFICULTIES)}")
 
 
def choose_bet(money):
    """Ask how much to bet. Returns a whole number."""
    # Percent of wallet, but never below MIN_BET or above what you own.
    safe = min(money, max(MIN_BET, money * 10 // 100))
    normal = min(money, max(MIN_BET, money * 25 // 100))
    risky = min(money, max(MIN_BET, money * 50 // 100))
    options = {f"1": safe, f"2": normal, f"3": risky, f"4": money}
 
    print(f"\nPlace your bet! You have ${money:,}.")
    print(f"  [1] Safe     (10% of wallet)  ${safe:,}")
    print(f"  [2] Normal   (25% of wallet)  ${normal:,}")
    print(f"  [3] Risky    (50% of wallet)  ${risky:,}")
    print(f"  [4] ALL-IN   (everything)     ${money:,}")
    print(f"  [5] Custom amount (${MIN_BET}-${money:,})")
 
    while True:
        choice = input(f"Pick a bet option (1-5): ").strip()
 
        if choice in options:
            return options[choice]
 
        if choice == f"5":
            raw = input(f"Enter your bet (${MIN_BET}-${money:,}): ").strip()
            try:  # int("abc") would crash, so we try it and catch the error
                amount = int(raw)
            except ValueError:
                print(f"That's not a whole number.")
                continue  # back to the top of the loop
            if MIN_BET <= amount <= money:  # chained comparison
                return amount
            print(f"Your bet must be between ${MIN_BET} and ${money:,}.")
            continue
 
        print(f"Please pick 1, 2, 3, 4 or 5.")
 
 
def hub(player):
    """The menu between rounds. Returns 'play' or 'quit'."""
    while True:
        show_wallet(player)
        print(f"\n  [1] Play a round")
        print(f"  [2] Visit the shop")
        print(f"  [3] Cash out and quit")
        choice = input(f"> ").strip()
 
        if choice == f"1":
            return f"play"
        elif choice == f"2":
            shop(player)
        elif choice == f"3":
            return f"quit"
        else:
            print(f"Please pick 1, 2 or 3.")
 
 
# ----------------------------------------------------------------------------
# PAYOUTS
# ----------------------------------------------------------------------------
def settle_bet(player, bet, multiplier, won, guesses_left, hints_used, active):
    """Pay out (or take) the bet at the end of a round and show the math."""
    double_down = f"double_down" in active  # "in" works on lists too
    safety_net = f"safety_net" in active
 
    print(f"\n--- Bet result (you bet ${bet:,}) ---")
 
    if won:
        base = round(bet * multiplier)
        speed = round(bet * SPEED_BONUS_RATE * guesses_left)
        penalty = round(bet * HINT_PENALTY_RATE * hints_used)
        profit = max(0, base + speed - penalty)  # never below zero
 
        print(f"  Base winnings ({multiplier:g}x):   +${base:,}")
        print(f"  Speed bonus ({guesses_left} guesses unused): +${speed:,}")
        print(f"  Hint penalty ({hints_used} hints used):   -${penalty:,}")
        if double_down:
            profit *= 2  # *= multiplies the variable in place
            print(f"  Double Down doubles your winnings!")
        player[f"money"] += profit  # += adds to the variable in place
        print(f"You WIN ${profit:,}!")
    else:
        loss = bet * 2 if double_down else bet
        loss = min(loss, player[f"money"])  # can't lose more than you own
        if double_down:
            print(f"  Double Down doubles your loss...")
        if safety_net:
            refund = loss // 2
            loss -= refund
            print(f"  Safety Net refunds ${refund:,}!")
        player[f"money"] -= loss
        print(f"You LOSE ${loss:,}.")
 
    money = player[f"money"]
    print(f"Wallet: ${money:,}")
 
 
# ----------------------------------------------------------------------------
# POWER-UPS AND SHOP
# ----------------------------------------------------------------------------
def pick_preround_powerups(player):
    """Before a round: offer power-ups that must be switched on first."""
    active = []  # keys of the power-ups the player turns on
    inventory = player[f"inventory"]
    for key in PRE_ROUND_ITEMS:
        if inventory[key] > 0:
            item = SHOP_ITEMS[key]
            print(f"\nYou own {inventory[key]} x {item[f'name']}: {item[f'desc']}")
            answer = input(f"Use one this round? (y/n): ").strip().lower()
            if answer == f"y":
                inventory[key] -= 1
                active.append(key)
                print(f"{item[f'name']} activated!")
    return active
 
 
def choose_round_powerup(player):
    """During a round: pick a power-up to use. Returns its key, or None."""
    inventory = player[f"inventory"]
    usable = [key for key in ROUND_ITEMS if inventory[key] > 0]
 
    if not usable:
        print(f"You don't own any usable power-ups. Visit the shop between rounds!")
        return None  # None means "nothing"
 
    print(f"Your power-ups:")
    # enumerate(..., start=1) gives a counter (1, 2, 3...) along with each item
    for number, key in enumerate(usable, start=1):
        item = SHOP_ITEMS[key]
        print(f"  [{number}] {item[f'name']} x{inventory[key]} - {item[f'desc']}")
 
    raw = input(f"Pick a number (or press Enter to cancel): ").strip()
    try:
        index = int(raw)
    except ValueError:
        print(f"Cancelled.")
        return None
    if not 1 <= index <= len(usable):
        print(f"Cancelled.")
        return None
 
    key = usable[index - 1]  # lists count from 0, our menu counts from 1
    inventory[key] -= 1
    return key
 
 
def shop(player):
    """The between-rounds shop."""
    inventory = player[f"inventory"]
    keys = list(SHOP_ITEMS)  # list of the item keys, so we can number them
 
    while True:
        money = player[f"money"]
        print(f"\n=== POWER-UP SHOP ===   (you have ${money:,})")
        for number, key in enumerate(keys, start=1):
            item = SHOP_ITEMS[key]
            print(f"  [{number}] {item[f'name']:<13} ${item[f'price']:<4} (own {inventory[key]})  {item[f'desc']}")
        print(f"  [0] Leave the shop")
 
        raw = input(f"Buy which item? ").strip()
        try:
            choice = int(raw)
        except ValueError:
            print(f"Type a number from the menu.")
            continue
 
        if choice == 0:
            return
        if not 1 <= choice <= len(keys):
            print(f"Type a number from the menu.")
            continue
 
        key = keys[choice - 1]
        item = SHOP_ITEMS[key]
        price = item[f"price"]
 
        # Don't let the player spend themselves into bankruptcy.
        if money - price < MIN_BET:
            print(f"You must keep at least ${MIN_BET} to play. You can't afford that.")
        else:
            player[f"money"] -= price
            inventory[key] += 1
            print(f"Bought {item[f'name']} for ${price}!")
 
 
# ----------------------------------------------------------------------------
# BANKRUPTCY PENALTY
# ----------------------------------------------------------------------------
def bankruptcy_penalty(player):
    """Type out random numbers. One typo = start from scratch."""
    border = f"#" * 50  # "*" repeats text
    print(f"\n{border}")
    print(f"#{f'YOU ARE BANKRUPT!':^48}#")  # :^48 centers the text
    print(f"{border}")
    print(f"To earn a ${BAILOUT_MONEY} bailout you must type out {TYPING_COUNT} random numbers.")
    print(f"Type each number EXACTLY as shown. ONE typo and you start over!\n")
    input(f"Press Enter when you're ready to begin...")
 
    attempt = 1
    while True:
        # Make TYPING_COUNT random 4-digit numbers. "_" = a name we don't use.
        numbers = [random.randint(1000, 9999) for _ in range(TYPING_COUNT)]
 
        all_correct = True  # a True/False "flag"
        for position, number in enumerate(numbers, start=1):
            typed = input(f"[{position}/{TYPING_COUNT}] Type this number: {number}  > ").strip()
            if typed != f"{number}":  # compare text with text
                print(f"\nTYPO! You typed '{typed}' but it was {number}.")
                print(f"Starting over with brand new numbers...\n")
                all_correct = False
                break  # stop this attempt right away
 
        if all_correct:
            break  # done, leave the loop
        attempt += 1
 
    player[f"money"] = BAILOUT_MONEY
    print(f"\nPerfect! That took {attempt} attempt(s).")
    print(f"The bank gives you a ${BAILOUT_MONEY} bailout. Bet wisely this time!")
 
 
# ----------------------------------------------------------------------------
# PLAYING A ROUND
# ----------------------------------------------------------------------------
def play_round(player):
    difficulty = choose_difficulty()
    low, high, max_guesses, max_hints = DIFFICULTIES[difficulty]  # unpack the tuple
    multiplier = PAYOUT_MULTIPLIERS[difficulty]
 
    # Bet BEFORE the bonus roll, so you never know when the jackpot is coming.
    bet = choose_bet(player[f"money"])
    active = pick_preround_powerups(player)
 
    # Secret bonus mode: insane difficulty AND a lucky roll.
    # random.random() gives a decimal from 0.0 to 1.0.
    is_bonus = False
    if difficulty == f"insane" and random.random() < BONUS_CHANCE:
        is_bonus = True
        low, high, max_guesses, max_hints = BONUS_MODE
        multiplier = BONUS_MULTIPLIER
 
        border = f"*" * 46
        print(f"\n{border}")  # \n = new line
        print(f"*{f'':^44}*")
        print(f"*{f'*** SECRET BONUS MODE UNLOCKED ***':^44}*")
        print(f"*{f'':^44}*")
        print(f"*{f'A 1 in {round(1 / BONUS_CHANCE)} chance... and you got it!':^44}*")
        print(f"*{f'Only the luckiest ever see this.':^44}*")
        print(f"*{f'':^44}*")
        print(f"{border}")
        print(f"\nThe range just exploded to {low}-{high}.")
        print(f"Your winnings multiplier jumps to {multiplier:g}x!")
        print(f"You get {max_guesses} guesses and {max_hints} hints. Good luck!")
 
    secret = random.randint(low, high)  # includes both ends
    hints = build_hints(secret, low, high)
    hints_used = 0
    previous_guess = None  # nothing yet (used for warmer/colder)
 
    print(f"\nI'm thinking of a number between {low} and {high}. You bet ${bet:,}.")
    print(f"You have {max_guesses} guesses. Commands: 'hint' (math hint, costs winnings), "
          f"'use' (power-ups), 'quit' (forfeit your bet).\n")
 
    guesses_left = max_guesses
 
    while guesses_left > 0:
        raw = input(f"[{guesses_left} guesses left] Your guess: ").strip().lower()
 
        # --- quit: forfeit the bet ---
        if raw == f"quit":
            print(f"You forfeit. The number was {secret}.")
            settle_bet(player, bet, multiplier, False, guesses_left, hints_used, active)
            return
 
        # --- hint ---
        if raw == f"hint":
            available = min(max_hints, len(hints))  # never more hints than exist
            if hints_used >= available:
                print(f"No hints left!")
            else:
                print(f"Hint {hints_used + 1}/{available}: {hints[hints_used]}")
                hints_used += 1
            continue  # skip to the next loop pass without using a guess
 
        # --- power-up ---
        if raw == f"use":
            powerup = choose_round_powerup(player)
            if powerup == f"extra_guess":
                guesses_left += 1
                print(f"Extra Guess! You now have {guesses_left} guesses left.")
            elif powerup == f"bonus_hints":
                max_hints += 2
                print(f"Bonus Hints! You can now ask for {max_hints} hints.")
            elif powerup == f"range_finder":
                start, end = find_range_window(secret, low, high)
                print(f"Range Finder: the number is between {start} and {end}.")
            continue
 
        # --- a guess: turn the text into a number ---
        try:
            guess = int(raw)
        except ValueError:
            print(f"Enter a whole number, 'hint', 'use', or 'quit'.")
            continue
 
        if not low <= guess <= high:
            print(f"Stay within {low}-{high}.")
            continue
 
        guesses_left -= 1
 
        if guess == secret:
            print(f"\nCorrect! The number was {secret}.")
            if is_bonus:
                print(f"*** BONUS MODE CONQUERED! You're a legend. ***")
            settle_bet(player, bet, multiplier, True, guesses_left, hints_used, active)
            return
 
        word, direction = (f"low", f"higher") if guess < secret else (f"high", f"lower")
        print(f"Too {word} - go {direction}.")
 
        # abs() drops the minus sign, so abs(guess - secret) is the distance.
        if previous_guess is not None:
            if abs(guess - secret) < abs(previous_guess - secret):
                print(f"  (warmer)")
            elif abs(guess - secret) > abs(previous_guess - secret):
                print(f"  (colder)")
        previous_guess = guess
 
    # Reached only when the loop ends because guesses ran out.
    print(f"\nOut of guesses! The number was {secret}.")
    settle_bet(player, bet, multiplier, False, 0, hints_used, active)
 
 
# ----------------------------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------------------------
def main():
    print(f"=== Number Guessing Game ===")
    print(f"You start with ${STARTING_MONEY}. Bet on your guesses, buy power-ups,")
    print(f"and whatever you do... don't go bankrupt.")
 
    player = new_player()
 
    while True:
        if player[f"money"] < MIN_BET:
            bankruptcy_penalty(player)
 
        if hub(player) == f"quit":
            break  # leaves the loop and ends the game
        play_round(player)
 
    net = player[f"money"] - STARTING_MONEY
    # {net:+,} shows a + or - sign
    print(f"\nYou cashed out with ${player[f'money']:,} ({net:+,} compared to the start).")
    print(f"Thanks for playing!")
 
 
# Runs main() only when you run this file directly (not when it's imported).
if __name__ == f"__main__":
    main()
 