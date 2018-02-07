import re
import sys

file =""
pattern = ".*"
count = 0 
# Open the file with read only permit
if len(sys.argv) > 1 :
    file = open(sys.argv[1])
    for a in range(2, len(sys.argv)) :
        pattern = pattern +sys.argv[a]+".*"

#print("Pattern:"+pattern)

if file:
    # use readline() to read the first line 
    #line = file.readline()
    lines = file.readlines()
    
    for ln in lines:
        if re.search(pattern,ln, re.IGNORECASE):
            if count == 0:
                print("Matched line(s)...")
            print("["+ln+"]")
            count = count+1
    file.close()
    
    print("Total matched:"+str(count))
