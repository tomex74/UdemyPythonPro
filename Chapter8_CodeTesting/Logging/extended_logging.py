# pip install loguru
# Github: https://github.com/Delgan/loguru#no-handler-no-formatter-no-filter-one-function-to-rule-them-all
from pathlib import Path

from loguru import logger

@logger.catch
def my_function(x, y, z):
    logger.info("Entering my function")
    result = 1 / (x + y + z)
    logger.info("Leaving my function")
    return result

def main():
    file_path = Path(__file__).parent.joinpath('log3.log')
    logger.add(file_path, rotation="10KB", retention=1)

    logger.info("Start logging")
    my_function(-1.0, 0, 1)

if __name__ == '__main__':
    main()
