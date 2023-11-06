# UpworkPortfolioProjectFiller
Fills and formats upwork protfolio project descriptions that normally prevent copying and pasting from an outside text file

Automate Form Filling Using PyAutoGUI
This Python script is designed to automate the process of filling out web forms, especially when you encounter restrictions on copying and pasting into a form, as commonly seen on websites like Upwork and others. By leveraging the PyAutoGUI library, this script simulates user input to streamline the data entry process.

markdown
Copy code
# PyAutoGUI Keystroke Automation for Form Filling

## Overview

This Python script utilizes the PyAutoGUI library to automate keystrokes and tackle the issue of encountering restrictions on copying and pasting into a form, as commonly seen on websites like Upwork and others. By leveraging the PyAutoGUI library, this script simulates user input to streamline the data entry process.

## Problem Statement

Many websites, including popular platforms like Upwork, implement security measures that prevent users from copying and pasting text into their forms. This restriction can be frustrating, especially when you have large amounts of data to input. This script provides an elegant solution by automating the keystrokes required to enter text, effectively bypassing the copy-paste restrictions.

## Prerequisites

Before running this script, ensure that you have Python and the PyAutoGUI library installed on your system. You can install PyAutoGUI using pip:

```bash
pip install pyautogui

Usage
Open the web page or application where you want to input text.

Position your cursor in the appropriate text field where you want to input the text.

Run the script using Python. You may need to adjust the initial delay to give yourself enough time to switch to the correct window.

python
Copy code
python automate_keystrokes.py
The script will automatically type out the lines of text specified in the lines_to_write list one by one, simulating manual keystrokes. It also presses 'Enter' after each line to create a new line.

Sit back and let the script do the typing for you! This is especially useful when websites prevent you from directly copying and pasting text into their forms.

Customization
You can customize the lines_to_write list in the script to include the specific text you want to input into the form. Modify this list with your desired content.

python
lines_to_write = [
    "Desired text",
    "Formatted Line by Line",
    "• bullets included if desired."    
]
You can also adjust the pause time between PyAutoGUI commands by changing the pyautogui.PAUSE value to match your preferences.

python
pyautogui.PAUSE = 0.5  # Adjust the pause time (in seconds) between commands
Disclaimer
Please use this script responsibly and only on websites and applications where automating keystrokes is allowed and in compliance with their terms of service. Be aware that some websites may have security measures in place to detect and prevent automation.

Author
Gerardo "Jerry" Valdez
