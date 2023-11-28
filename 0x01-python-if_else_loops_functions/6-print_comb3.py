#!/bin/python3
for tens in range(0, 8):
    for units in range(0, 10):
        if tens != units and tens < units:
            print(f"{tens}{units}", end=', ')
print(89)
