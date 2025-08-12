import sys
import time
import os

# Colors for CMD (white text, can adjust)
RESET = "\033[0m"
WHITE = "\033[97m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
GRAY = "\033[90m"

def type_text(text, delay=0.04, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
    sys.stdout.flush()

def blink_text(text, blink_times=10, delay=0.5):
    for _ in range(blink_times):
        sys.stdout.write(text)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\r" + " " * len(text) + "\r")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(text + "\n")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()
sys.stdout.write(WHITE + "Microsoft Windows [Version 10.0.22631.4169]\n" + RESET)
sys.stdout.write(WHITE + "(c) Microsoft Corporation. All rights reserved.\n\n" + RESET)

type_text(WHITE + "C:\\Users\\Namig> py HelloWorld.py" + RESET, delay=0.04)
time.sleep(0.5)

# PROFILE HEADER
type_text(CYAN + "\n╔═════════════════════════════╗", 0.002)
type_text("║      " + YELLOW + "DEVELOPER PROFILE" + CYAN + "       ║", 0.002)
type_text("╚═════════════════════════════╝" + RESET, 0.002)
time.sleep(0.5)

# Intro
type_text(GREEN + "Hey there! " + RESET + "I'm " + MAGENTA + "Namig Akhundov" + RESET, 0.05)
type_text(GRAY + "4th year CS student | junior Data Analyst | Future AI/ML enthusiast" + RESET, 0.03)
time.sleep(0.5)

# Languages with proficiency
type_text(CYAN + "\nLanguages:" + RESET, 0.05)
langs = [
    ("Azerbaijani", "native"),
    ("Russian", "native"),
    ("English", "advanced")
]
for lang, prof in langs:
    type_text(f"  - {GREEN}{lang}{RESET} ({YELLOW}{prof}{RESET})", 0.04)
    time.sleep(0.15)

# Skills (new, fresher)
time.sleep(0.4)
type_text(CYAN + "\nCore Skills:" + RESET, 0.05)
skills = ["Algorithm Design", "Problem Solving", "System Architecture"]
for skill in skills:
    type_text(f"  - {YELLOW}{skill}{RESET}", 0.04)
    time.sleep(0.15)

# Programming & Frameworks
time.sleep(0.5)
type_text(CYAN + "\nProgramming & Frameworks:" + RESET, 0.05)
prog = [
    (MAGENTA + "Python" + RESET + ": Django, NumPy, Pandas, Matplotlib"),
    (MAGENTA + "Java" + RESET),
    (MAGENTA + "C/C++" + RESET),
    (MAGENTA + "ARM Assembly" + RESET),
]
for p in prog:
    type_text(f"  - {p}", 0.04)
    time.sleep(0.15)

# Web Development
time.sleep(0.5)
type_text(CYAN + "\nWeb Development:" + RESET, 0.05)
web = [
    (YELLOW + "JavaScript" + RESET + ": React, 3JS, React Native Expo"),
    ("HTML, CSS, Tailwind CSS, GSAP"),
]
for w in web:
    type_text(f"  - {w}", 0.04)
    time.sleep(0.15)

# Database Technologies
time.sleep(0.5)
type_text(CYAN + "\nDatabase Technologies:" + RESET, 0.05)
db = [
    (YELLOW + "SQL" + RESET + ": MySQL, PostgreSQL"),
]
for d in db:
    type_text(f"  - {d}", 0.04)
    time.sleep(0.15)

# Data Visualization
time.sleep(0.5)
type_text(CYAN + "\nData Visualization:" + RESET, 0.05)
viz = [
    ("Tableau, Power BI, MS Office"),
]
for v in viz:
    type_text(f"  - {v}", 0.04)
    time.sleep(0.15)

# Operating Systems
time.sleep(0.5)
type_text(CYAN + "\nOperating Systems:" + RESET, 0.05)
osys = ["Windows", "Linux"]
for o in osys:
    type_text(f"  - {GREEN}{o}{RESET}", 0.04)
    time.sleep(0.15)

# Version Control
time.sleep(0.5)
type_text(CYAN + "\nVersion Control:" + RESET, 0.05)
type_text(f"  - {YELLOW}Git{RESET}", 0.04)

time.sleep(0.6)
blink_text(YELLOW + ">>> Scroll down to see more <<<" + RESET, blink_times=10, delay=0.4)
