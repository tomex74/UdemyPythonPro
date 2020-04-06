# pip install loguru
# Github: https://github.com/Delgan/loguru#no-handler-no-formatter-no-filter-one-function-to-rule-them-all
from pathlib import Path

from loguru import logger

@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)

def main():
    file_path = Path(__file__).parent.joinpath('log3.log')
    logger.add(file_path, rotation="1 MB")

    logger.debug("That's it, beautiful and simple logging!")
    logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")
    my_function(-1, 0, 1)

if __name__ == '__main__':
    main()
