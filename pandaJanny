#! python3

from pathlib import Path
import os
import re

# Expected metadata
# (\(comiket\))? \[circle \(artist\)\])? title (series) [language] [translator]

doujinPattern = re.compile(
        r'(\(.*\))? (\[.*\])? (.*) (\(.*\))? (\[.*\])? (\[.*\])?'
        ) # this regexp sucks btw

print('Hello! Point me to the location of all your sadpandas')
while True:
    workingDir = input('Input path: ')
    try:
        os.chdir(workingDir)
    except:
        print('This path does not exist, please try again')
        continue
    break

for doujinDir in Path.listdir(workingDir):
    
    doujinInfo = doujinPattern.search(str(doujinDir)) # get the metadata with regex from directory name
    
    os.chdir(doujinDir)

    rawTags = open('rawTags','w')
    # TODO maybe do some editing on the search results
    # TODO write each group as separate line in the file, prefixed with correct namespace
    rawTags.close()

    os.chdir('..')
print('All done, thank you for waiting')
