import logging
from functools import wraps
from pathlib import Path
from datetime import datetime

def logged(fn, name=None, message=None):
    @wraps(fn)
    def decorate(*args, **kwargs):
        dt = datetime.utcnow()
        name = fn.__name__
        result = fn(*args, **kwargs)
        print('{0}: called {1} = {2}'.format(dt, name, result))
        return result
    return decorate

@logged
def add(a, b):
    return a + b 

def main():
    add(2, 3)

if __name__ == '__main__':
    main()
