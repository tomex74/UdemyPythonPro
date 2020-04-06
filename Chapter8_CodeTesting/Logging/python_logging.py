import logging
from pathlib import Path

def do_something():
    logging.info('Doing something')

def main():
    file_path = Path(__file__).parent.joinpath('log1.log')
    logging.basicConfig(filename=file_path, level=logging.INFO)
    logging.info('Logging into file: %s', file_path.name)
    logging.info('Started')
    do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
