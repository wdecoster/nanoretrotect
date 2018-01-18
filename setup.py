# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


exec(open('nanoretrotect/version.py').read())


setup(
    name='nanoretrotect',
    version=__version__,
    description='',
    long_description=open(path.join(here, "README.rst")).read(),
    url='https://github.com/wdecoster/nanoretrotect',
    author='Wouter De Coster',
    author_email='decosterwouter@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='',
    python_requires='>=3',
    packages=find_packages(),  # + ['scripts'],
    install_requires=['pandas', 'numpy', 'NanoPlot>=0.19.1',
                      'nanoget>=1.3.0', 'nanoplotter>=0.30.1'],
    package_dir={'nanoretrotect': 'nanoretrotect'},
    entry_points={
        'console_scripts': [
            'nanoretrotect=nanoretrotect.nanoretrotect:main',
        ],
    }
)
