#! python3

from pathlib import Path
import os
import re

# The regexp for extracting metadata
doujinPattern = re.compile(r'''
    (\(.*\))? # when it was released
    (\[.*\])? # circle name (with artist)
    (.*) # title
    (\(.*\))? # series this is based upon
    (\[.*\])? # language
    (\[.*\])? # translation group
    ''', re.VERBOSE) # this regexp sucks btw

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
    print(' - ' + str(doujinDir))
    doujinInfo = doujinPattern.search(str(doujinDir)) # get the metadata with regex from directory name
    os.chdir(doujinDir)

    rawTags = open('rawTags','w')
    # TODO maybe do some editing on the search results
    # TODO write each group as separate line in the file, prefixed with correct namespace
    rawTags.close()
    os.chdir('..')
    print('done')
    
print('All done, thank you for waiting')
