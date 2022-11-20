#command line utility

import argparse
import sys

def cal(args):
    if args.o =='add':
        return args.x + args.y
    if args.o == 'sub':
        return args.x - args.y
    if args.o == 'multi':
        return args.x * args.y
    if args.o == 'div':
        return args.x / args.y
    else:
        return "somthing went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float,
                        default=1.0,
                        help="enter first number:")

    parser.add_argument('--y', type=float,
                        default=3,help="enter second number: ")

    parser.add_argument('--o', type=str,
                        default="add",help="this is a utility calculation")

args = parser.parse_args()
sys.stdout.write(str(cal(args)))


#==========================================================================================================

