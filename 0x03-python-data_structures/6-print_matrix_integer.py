#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(the_matrix=[[]]):
    for x in range(len(the_matrix)):
        for j in range(len(the_matrix[x])):
                print("{:d}".format(the_matrix[x][j]), end="")
                if j != (len(the_matrix[x]) - 1):
                    print(" ", end="")

        print("")
