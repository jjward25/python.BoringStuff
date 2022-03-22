import zipfile, os

def backupToZip(folder):
    # back up the entire contents of "folder" into a Zip file
    folder = os.path.abspath(folder) # make sure folder is absolute

    ## figure out the filename based on the filenames already in the folder
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number +1

    ## Create the zip file 
    print(f'Creating {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName,'w')

    ## Walk the folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding fils in {foldername}...')
        backupZip.write(foldername)
        ## add all files in this folder to the zip file
        for filename in filenames:
            newBase = os.path.basename(folder + '_')
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the backup zip files
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
print('Done.')

backupToZip('C:/Users/Josep/OneDrive/Desktop/Nutshell/')

## backs up everything passed to the function in line 32 and saves the output in the current working directory