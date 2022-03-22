import webbrowser, sys, pyperclip
if len(sys.argv) > 1:  ## checks that you entered something besides just mapit
    #Get sddress from command line.
    address = ''.join(sys.argv[1:])  ## selecting from the second item in the array removes the function call (mapit)

#Get address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('https://'+address+'/')

