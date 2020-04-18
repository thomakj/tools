import argparse


parser = argparse.ArgumentParser()

parser.add_argument("ascii_nums", type=str)
args = parser.parse_args()

print(''.join(chr(int(i)) for i in args.ascii_nums.split(' ')))
