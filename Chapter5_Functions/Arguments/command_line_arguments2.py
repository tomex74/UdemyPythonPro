import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Add the values val1, val2 and val3')
    parser.add_argument("--val1", help='first value', type=int, required=True, dest='val1')
    parser.add_argument("--val2", help='second value', type=int, required=True, dest='val2')
    parser.add_argument("--val3", help='third value', type=int, required=True, dest='val3')
    args = parser.parse_args()
    print(args)
    print(args.val1)
    print(args.val2)
    print(args.val3)

# python command_line_arguments2.py --val1 10 --val2 20 --val3 30
if __name__ == "__main__":
    main()