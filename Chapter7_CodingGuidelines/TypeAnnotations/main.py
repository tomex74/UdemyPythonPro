"""Test code.
"""
from vector_type_annotations import Vector2D


def print_value(val: str):
    print(val)


def main():
    v1 = Vector2D(2, 5)
    test= v1 * 7
    print(test)




if __name__ == "__main__":
    main()
