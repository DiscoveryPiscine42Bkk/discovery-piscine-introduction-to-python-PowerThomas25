
import sys

args = sys.argv[1:]

if len(args) != 2:
    print ("de kub")
else:
    word = args[0] 
    text = args[1]
    count = text.split ().count(word)
    print(count)