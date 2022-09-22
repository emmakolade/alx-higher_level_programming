#!/usr/bin/python3
# print the alphabet in lowercase, not followed by a new line
for i in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(i), end='')
