"""Reading a file with Morse code and sending it to morse_code.py."""

import morse_code
import sys

def main():
    with open(sys.argv[1], 'r') as file:
        for line in file:
            print(morse_code.from_morse(line))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        exit("Please include file as argument")

    main()
