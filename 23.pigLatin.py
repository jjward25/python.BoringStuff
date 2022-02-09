print('Enter the English message to translate to Pig Latin:')
message = input()

wordList = message.split()
print(wordList)

pigLatin = []

for word in wordList:
    if word[0].lower() == 'a':
        word = word + 'yay'
        pigLatin.append(word)
    elif word[0].lower() == 'e':
        word = word + 'yay'
        pigLatin.append(word)
    elif word[0].lower() == 'i':
        word = word + 'yay'
        pigLatin.append(word)
    elif word[0].lower() == 'o':
        word = word + 'yay'
        pigLatin.append(word)
    elif word[0].lower() == 'u':
        word = word + 'yay'
        pigLatin.append(word)
    elif word[0].lower() == 'y':
        word = word + 'yay'
        pigLatin.append(word)
    else:
        word = word[1:] + word[0] + 'ay'
        pigLatin.append(word)

newMessage = ' '.join(pigLatin)

print(newMessage)