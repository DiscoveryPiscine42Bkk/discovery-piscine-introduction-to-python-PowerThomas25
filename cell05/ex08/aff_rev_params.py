import sys

args = sys.argv[1:]
if len(args) == 0:
    print("eiein")
else:
    for arg in reversed (args):
        print(arg)