#!/usr/bin/python3
# prints the sum of its arguments

if __name__ == "__main__":
    sum = 0
    from sys import argv

    for arg in argv[1:]:
        sum = sum + int(arg)
    print(sum)
