import sys
def main():Add commentMore actions
    if len(sys.argv) != 2:
        print("none")
        return

    text = sys.argv[1]
    count_z = text.count('z')

    if count_z == 0:
        print("none")
    else:
        print('z' * count_z)

if __name__ == "main":
    main()