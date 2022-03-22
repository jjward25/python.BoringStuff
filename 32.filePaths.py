###### CRUD #####
###### CRUD #####
###### CRUD #####
## Use shutil to copy, move, rename and delete existing files from folders
## shutil is good for deleting entire folders and their contents
## the os module (import os) can delete a single file or a single empty folder

# os.unlink(path) # will delete the file at path
# os.rmdir(path) #will delete the folder at path if it is empty
# shutil.rmtree(path) # will remove the folder at path
## best practice is to add these codes last and have them commented out w print statements to see what would be deleted
#### for filename in path.home().glob('*.rxt'):
    ## os.unlink(filename) commented out
    # print(filename) used as a check


## Safe deleting with the send2trash module (import send2trash)
## syntax is send2trash.send2trash('filename')

##### CRUD LOOP THROUGH FOLDERS #####
##### CRUD LOOP THROUGH FOLDERS #####
##### CRUD LOOP THROUGH FOLDERS #####
## os.walk(path) is used to open a folder and go through the files in that folder path, then walk through each subfolder
## os.walk() returns three values on each iteration: a string of the current folder's name, a list of strings of the folders in the current folder, and a list of strings of the files in the current folder

import os
#print(os.walk('C:/Users/Josep/OneDrive/Desktop/Coding/'))
for folderName, subfolders, filenames in os.walk('C:/Users/Josep/OneDrive/Desktop/Nutshell/'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('Subfolder of ' + folderName + ": " + subfolder)
        for filename in filenames:
            print('File inside ' + folderName + ': ' + filename)
            print('')

