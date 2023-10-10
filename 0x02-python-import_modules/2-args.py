#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leng = len(argv) - 1
    if leng == 1:
        print("{:d} argument:".format(leng))
    else:
        print("{:d} arguments:".format(leng))
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))