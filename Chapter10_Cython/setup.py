try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
from Cython.Build import cythonize

CLASSIFIERS = '''\
License :: OSI Approved
Programming Language :: Python :: 3.7 :: or higher
Topic :: Software Development
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
'''

DISTNAME = 'fastvector'
AUTHOR = 'Jan Schaffranek'
AUTHOR_EMAIL = 'jan.schaffranek@rub.com'
DESCRIPTION = 'This is an Example Package for math calculations.'
LICENSE = 'New BSD'

MAJOR = 0
MINOR = 2
MICRO = 0
ISRELEASED = True
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

PYTHON_MIN_VERSION = '3.7'
SCIPY_MIN_VERSION = '1.1.0'
NUMPY_MIN_VERSION = '1.14.0'

metadata = dict(
    name=DISTNAME,
    version=VERSION,
    packages=['fastvector', 'fastvector.test'],
    ext_modules=cythonize("./fastvector/cython_computations.pyx"),
    python_requires='>={}'.format(PYTHON_MIN_VERSION),
    install_requires=['numpy>={}'.format(NUMPY_MIN_VERSION),
                      'scipy>={}'.format(SCIPY_MIN_VERSION),],
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    classifiers=[CLASSIFIERS],
    license=LICENSE,
)

def setup_package():
    setup(**metadata)

if __name__ == '__main__':
    setup_package()
