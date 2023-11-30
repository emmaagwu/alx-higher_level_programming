#!/usr/bin/python3
# 2-args


if __name__ == "__main__":
    from sys import argv

    index = 1
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print(f"{len(argv) - 1} arguments:")

    for arg in argv[1:]:
        print(f"{index}: {arg}")
        index = index + 1
