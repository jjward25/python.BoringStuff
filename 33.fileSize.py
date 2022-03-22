##### Reading Compressed Files #####
##### Reading Compressed Files #####
##### Reading Compressed Files #####
## import zipfile, os
## exampleZip = zipfile.ZipFile('filename') ## this will read an already compressed file and create an object
## exampleZip.namelist() ## returns the list of files in the zip file/folder
## spamInfo = exampleZip.getinfo('spam.txt')
## spamInfo.file_size ## returns file size in bytes
## spamInfo.compress_size ## compressed size in bytes
## exampleZip.close()

##### Extracting from Compressed Files #####
##### Extracting from Compressed Files #####
##### Extracting from Compressed Files #####
## import zipfile, os
## from pathlib import Path
## p = Path.home()
## exampleZip = zipFile(p/'example.zip')
## exampleZip.extractall()
## exampleZip.close()

##### Creating and Adding to Zip Files #####
##### Creating and Adding to Zip Files #####
##### Creating and Adding to Zip Files #####
## import zipfile
## newZip = zipfile.ZipFile('new.zip','w')
## newZip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)
## newZip.close()

