import logging
from functools import wraps
from pathlib import Path

def logged(level, name=None, message=None):
    '''Add logging to a function.  level is the logging
    level, name is the logger name, and message is the
    log message.  If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.CRITICAL, 'example')
def add(a, b):
    return a + b 

def main():
    file_path = Path(__file__).parent.joinpath('log2.log')
    logging.basicConfig(filename=file_path, level=logging.INFO)
    print(add(2, 3))

if __name__ == '__main__':
    main()
