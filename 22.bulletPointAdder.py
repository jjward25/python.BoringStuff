## Take text from the clipboard
## Add an asterisk to the front of each string
## Copy the new text to the clipboard (wikipedia posts add bullets if you submit text with *'s in front)

#! python3
import pyperclip
text = pyperclip.paste()

## Seperate lines and add *'s
lines = text.split('\n')  # creates a list, separating the original text at each newline
for i in range(len(lines)): # loop through all indexes in the lines list
    lines[i] = "* " + lines[i]  # edits the text

# re-structure the text variable
text = '\n'.join(lines)

## Copy the new text
pyperclip.copy(text)

