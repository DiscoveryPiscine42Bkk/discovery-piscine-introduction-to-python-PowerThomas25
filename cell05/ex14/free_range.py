import sys
args = sys.argv[1:]
if len(args) != 2:
    print("none")Add commentMore actions
else:
    try:
        start = int(args[0])
        end = int(args[1])
        print(list(range(start, end + 1)))
    except valueError:
        print("none")