"""
🪄 PYTHON MAGIC TRICKS 🪄
A grab-bag of "how did that even work" terminal effects.
Run it, pick a spell, feel like a wizard.

No extra installs needed — pure Python standard library.
"""

import os
import sys
import time
import random
import math

# ---------------------------------------------------------
# Spell 1: Matrix digital rain
# ---------------------------------------------------------
def matrix_rain(duration=6):
    width = os.get_terminal_size().columns
    drops = [0] * width
    chars = "アイウエオカキクケコサシスセソ0123456789ABCXYZ$#@%"
    end_time = time.time() + duration
    print("\033[92m", end="")  # green text
    try:
        while time.time() < end_time:
            line = ""
            for i in range(width):
                if random.random() < 0.02:
                    drops[i] = 1
                if drops[i] > 0:
                    line += random.choice(chars)
                    drops[i] += 1
                    if drops[i] > random.randint(5, 20):
                        drops[i] = 0
                else:
                    line += " "
            print(line)
            time.sleep(0.05)
    finally:
        print("\033[0m", end="")  # reset color


# ---------------------------------------------------------
# Spell 2: Text that "types itself" then scrambles into place
# ---------------------------------------------------------
def scramble_reveal(text, rounds=15, delay=0.04):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    result = list(text)
    locked = [c == " " for c in text]

    for _ in range(rounds):
        line = ""
        for i, ch in enumerate(text):
            if locked[i]:
                line += ch
            else:
                line += random.choice(letters)
        print("\r" + line, end="", flush=True)
        time.sleep(delay)

        # lock in a few more letters each round
        unlocked = [i for i, l in enumerate(locked) if not l]
        for i in random.sample(unlocked, max(1, len(unlocked) // rounds)):
            locked[i] = True

    print("\r" + text)


# ---------------------------------------------------------
# Spell 3: A spinning ASCII donut (the classic show-off trick)
# ---------------------------------------------------------
def donut(frames=200):
    A, B = 0.0, 0.0
    while frames > 0:
        frames -= 1
        z = [0] * 1760
        b = [" "] * 1760
        for j in range(0, 628, 7):  # theta
            for i in range(0, 628, 2):  # phi
                c, d = math.sin(i / 100), math.cos(j / 100)
                e, f = math.sin(A), math.sin(j / 100)
                g, h = math.cos(A), math.cos(i / 100)
                D = 1 / (c * 2 + f * g + 5)
                l = math.cos(i / 100 * 2) * math.cos(B) - c * g * math.sin(B)
                m = c * g * math.cos(B) + math.cos(i / 100 * 2) * math.sin(B)
                n = d + 2
                x = int(40 + 30 * D * (h * n * math.cos(A) - m * math.sin(A)))
                y = int(12 + 15 * D * (h * n * math.sin(A) + m * math.cos(A)))
                o = x + 80 * y
                N = int(8 * ((f * g - c * h * d) * math.cos(B) - c * h * f - f * g * d - h * math.sin(B)))
                if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[N] if N > 0 else " "
        print("\033[H" + "\n".join("".join(b[k:k + 80]) for k in range(0, 1760, 80)))
        A += 0.08
        B += 0.03
        time.sleep(0.02)


# ---------------------------------------------------------
# Spell 4: "Predict" a number the user picked (real math trick!)
# ---------------------------------------------------------
def mind_reader():
    print("Think of a number between 1 and 63.")
    print("I'll show you 6 grids. Just tell me YES if your number is in the grid, else press Enter.\n")
    guess = 0
    bit = 1
    for i in range(6):
        grid = [n for n in range(1, 64) if n & (1 << i)]
        print(f"Grid {i+1}: {grid}")
        ans = input("Is your number here? (y/n): ").strip().lower()
        if ans == "y":
            guess += bit
        bit *= 2
    print(f"\n✨ Your number was... {guess}! ✨")


# ---------------------------------------------------------
# Menu
# ---------------------------------------------------------
if __name__ == "__main__":
    print("🪄 Choose your spell:")
    print("1) Matrix rain")
    print("2) Scramble reveal")
    print("3) Spinning donut")
    print("4) Mind reader (binary trick)")
    choice = input("> ").strip()

    if choice == "1":
        matrix_rain()
    elif choice == "2":
        scramble_reveal("YOU ARE NOW A PYTHON WIZARD")
    elif choice == "3":
        donut()
    elif choice == "4":
        mind_reader()
    else:
        print("No such spell yet. Add your own below!")