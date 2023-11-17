import pyautogui
import time

# Initial delay to allow you to switch to the window where you want to type
time.sleep(5)

# Set a default pause between pyautogui commands
pyautogui.PAUSE = 0.5

# List of strings to be written
lines_to_write = [
    "Desired text",
    "Formatted Line by Line",
    "• bullets included if desired."    
]

# Loop through each line and write it out, then press 'Enter'
for line in lines_to_write:
    pyautogui.write(line)
    pyautogui.press('enter')  # This creates a new line after each line of text
