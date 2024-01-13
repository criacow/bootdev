#!/usr/bin/python3

import sys

def main():
    count = 0
    letters = {}
    for line in sys.stdin:
        input = line.rstrip('\n')
#        print(input)
        lower = input.lower()
        count += len(input.split())
        for i in lower:
            if i in letters:
                letters[i] = letters[i] + 1
            else:
                letters[i] = 1
    print(count)
    print(letters)

main()
