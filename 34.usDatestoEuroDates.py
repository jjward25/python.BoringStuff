import shutil, os, re

## Create a regex that matches files with the US date format
datePattern = re.compile(r"""^(.*?)  ## all text before the date
((0|1)?\d)- ##one or two digits for the month
((0|1|2|3)?\d)- ##one or two digits for the day
((19|20)\d\d) # four digits for the year
(.*?)$
""",re.VERBOSE)

## Loop through filenames
## for amerFilename in os.listdir('.'):
##     mo = datePattern.search(amerFilename)
    #skip files without a date
##     if mo == None:
##         continue
    #get differnet parts of the filename
##     beforePart = mo.group(1)
##     monthPart = mo.group(2)
##     dayPart = mo.group(4)
##  yearPart = mo.group(6)
##     afterPart = mo.group(8)
    ## if the Match object returned from the search() method is None, then it will move to the next filename
    ## Otherwise the various string matches are stored in variables named above, gruoped based on the regex partitions
#### Form the european style filename
## euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

#### Get the full, absolute path
## absWorkingDir = os.path.abspath('.')
## amerFilename = os.path.join(absWorkingDir,amerFilename)
##  euroFilename = os.path.join(absWorkingDir,euroFilename)

#### Rename the files
## print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
## shutil.move(amerFilename,euroFilename) ## uncomment AFTER testing