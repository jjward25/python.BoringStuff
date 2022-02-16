## Copy a Matthew McCaugheny script to your clipboard and run this to count how many times they say 'alright'
import pyperclip
import re

text = pyperclip.paste()
matchList = []
print(text)
alrightRegex = re.compile(r'alright|Alright')
print(alrightRegex.findall(text))
print(len(alrightRegex.findall(text)))
