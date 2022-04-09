"""Script to decrypt and encode Morse code."""

import argparse

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        # Numbers
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  ' ': ' ',
        # Special
        '.': '.-.-.-',  ',': '--..--', '?': '..--..',
        '\'': '.----.', '!': '-.-.--', '/': '-..-.',
        '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-',
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
        '¿': '..-.-', '¡': '--...-'
        }
CODE_REVERSED = {value: key for key, value in CODE.items()}


def to_morse(text):
    """Convert text to Morse."""
    return ''.join(CODE.get(i.upper()) for i in text)


def from_morse(code):
    """Convert code to text."""
    return ''.join(CODE_REVERSED.get(i) for i in code.split())


def main():
    """Logic."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--decode", help="decode from morse", type=str)
    parser.add_argument("-e", "--encode", help="encode to morse", type=str)
    args = parser.parse_args()
    if args.encode is not None:
        print(to_morse(args.encode))
    elif args.decode is not None:
        print(from_morse(args.decode))


if __name__ == '__main__':
    main()
