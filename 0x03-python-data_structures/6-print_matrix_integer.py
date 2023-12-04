#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, element in enumerate(row):
            print(element, end="" if i == len(row) - 1 else " ")
        print()
