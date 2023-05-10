#!/usr/bin/python3
for alphabet_list in range(97, 123):
    if (alphabet_list != 101 and alphabet_list != 113):
        print("{:c}".format(alphabet_list), end='')
