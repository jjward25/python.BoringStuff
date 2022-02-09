#! python3
# 21.autoEmails.py - A multi-clipboard pasting program for easy emailing

TEXT = {
    'agree':"""Yes, I agree.  Sounds good to me.""",
    'busy':"""Sorry, can we do this later or next week?""",
    'upsell':"""Would you consider making this a monthly donation?"""
}

## TO handle the command line argument, we'll store them in the variable sys.argv
## The first item in sys.argv should be a string containing the program's filename, and second should be the first command line argument

import sys
if len(sys.argv)<2:
    print('Usage: must pass two arguments')
    sys.exit()
keyphrase = sys.argv[1] # first command line arg is the keyphrase

## Now that the keyphrase is stored as a string in the keyphrase variable, we need to check for it in the TEXT dictionary
## Command line arguments are those values that are passed during calling of program along with the calling statement. Thus, the first element of the array sys.argv() is the name of the program itself
import pyperclip
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('Keyphrase not found.')


## Options for running the script
## Open the command prompt and enter the full path and the argument for TEXT: C:\Users\Josep\OneDrive\Desktop\Coding\python.BoringStuff\21.autoEmails.py busy
## Press win + r and type 'py C:\Users\Josep\OneDrive\Desktop\Coding\python.BoringStuff\21.autoEmails.py agree' to copy the Agree message text from the command line
## 