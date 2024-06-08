import os
import time
import keyboard
import pyautogui
import json
import sys
import platform
import hashlib
from time import sleep
from datetime import datetime

from termcolor import colored
from colorant import Colorant
from mss import mss as mss_module

#Settings
TOGGLE_KEY = 'F1'  # Toggle on/off colorant key
XFOV = 80  # X-Axis FOV
YFOV = 80  # Y-Axis FOV
INGAME_SENSITIVITY = 0.2 # Replace this with the your in-game sensitivity value
FLICKSPEED = 1.07437623 * (INGAME_SENSITIVITY ** -0.9936827126)  # Calculate flick speed
MOVESPEED = 0.5 / (5 * INGAME_SENSITIVITY) # Calculate move speed

monitor = pyautogui.size()
CENTER_X, CENTER_Y = monitor.width // 2, monitor.height // 2

def main():
    os.system('title Apple')
    colorant = Colorant(CENTER_X - XFOV // 2, CENTER_Y - YFOV // 2, XFOV, YFOV, FLICKSPEED, MOVESPEED)
    print(colored('''
           ██▓███ ▓██   ██▓ ██▀███   █    ██  ███▄    █ 
          ▓██░  ██▒▒██  ██▒▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █ 
          ▓██░ ██▓▒ ▒██ ██░▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒
          ▒██▄█▓▒ ▒ ░ ▐██▓░▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒
          ▒██▒ ░  ░ ░ ██▒▓░░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░
          ▒▓▒░ ░  ░  ██▒▒▒ ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ 
          ░▒ ░     ▓██ ░▒░   ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒░
          ░░       ▒ ▒ ░░    ░░   ░  ░░░ ░ ░    ░   ░ ░ 
          ░ ░        ░        ░              ░ 
          ░ ░                                                                                                                 
                                              Apple - v1.1''', 'magenta'))
    print()
    print(colored('[Info]', 'cyan'), colored('Set enemies to', 'white'), colored('Purple', 'magenta'))
    print(colored('[Info]', 'cyan'), colored(f'Press {colored(TOGGLE_KEY, "magenta")} to toggle ON/OFF Colorant', 'white'))
    print(colored('[Info]', 'cyan'), colored(f'Press', 'white'), colored('F2', 'magenta'), colored('to toggle ON/OFF Detection Window', 'white'))
    print(colored('[Info]', 'cyan'), colored('RightMB', 'magenta'), colored('= Aim,', 'white'))
    print(colored('[Info]', 'cyan'), colored('LeftAlt', 'magenta'), colored('= TB,', 'white'))
    print(colored('[Info]', 'cyan'), colored('F10', 'magenta'), colored('= SAim', 'white'))
    status = 'Disabled'
    
    try:
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                colorant.toggle()
                status = 'Enabled ' if colorant.toggled else 'Disabled'
            print(f'\r{colored("[Status]", "green")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'green'), colored('Exiting...', 'white') + '\n')
    finally:
        colorant.close()

if __name__ == '__main__':
    main()

#564646464547