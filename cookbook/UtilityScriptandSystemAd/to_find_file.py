'''   
You need to write a script that involves finding files, like a file renaming script or a log
archiver utility, but you’d rather not have to call shell utilities from within your Python
script, or you want to provide specialized behavior not easily available by “shelling out.
'''

#!/usr/bin/env python3.3 
import os 
import sys 


def findfile(start, name):
    for relpath, dirs, files  in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.normpath(os.path.abspath(full_path)))

if __name__ == "__main__":
    findfile(sys.argv[1], sys.argv[2])           
