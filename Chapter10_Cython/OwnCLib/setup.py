try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    from distutils.core import setup, find_packages, Extension
from Cython.Build import cythonize

CLASSIFIERS = '''\
License :: OSI Approved
Programming Language :: Python :: 3.6 :: or higher
Topic :: Software Development
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
'''

DISTNAME = 'fast_math'
AUTHOR = 'Jan Schaffranek'
AUTHOR_EMAIL = 'jan.schaffranek@rub.com'
DESCRIPTION = 'This is an Example Package for math calculations.'
LICENSE = 'New BSD'

MAJOR = 0
MINOR = 3
MICRO = 0
ISRELEASED = True
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

PYTHON_MIN_VERSION = '3.6'
SCIPY_MIN_VERSION = '1.1.0'
NUMPY_MIN_VERSION = '1.14.0'

# Cython and C API Code
CYTHON_FILES = cythonize(['./fast_math/cython_computations.pyx'])
C_API_FILES = cythonize(Extension('FastMathComputations',
                                  sources=['./fast_math/c_api_computations.c']))
EXT_MODULES = CYTHON_FILES + C_API_FILES

metadata = dict(
    name=DISTNAME,
    version=VERSION,
    packages=['fast_math'],
    ext_modules=EXT_MODULES,
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
