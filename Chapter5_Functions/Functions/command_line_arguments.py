import sys

def main():
    print(sys.argv)
    user_args = sys.argv[1:]
    print(user_args)
    # Values are always strings!
    for arg in user_args:
        print(type(arg), arg)

# python command_line_arguments.py 10 20 30
# python command_line_arguments.py --val1 10 --val2 20 --val3 30
if __name__ == "__main__":
    main()