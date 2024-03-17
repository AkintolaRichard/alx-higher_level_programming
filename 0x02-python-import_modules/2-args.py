#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    num = len(sys.argv) - 1
    print("{} ".format(num), end="")
    if num == 0:
        print("arguments.")
    elif num == 1:
        print("argument:")
    elif num > 0:
        print("arguments:")
    for i in range(1, num + 1):
        print("{}: {}".format(i, sys.argv[i]))
