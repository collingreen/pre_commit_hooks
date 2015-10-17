from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_hooks',
    description='hooks for pre-commit.',
    url='https://github.com/collingreen/pre-commit-hooks',
    version='0.0.1',

    author='Collin Green',
    author_email='collin@collingreen.com',

    platforms='osx',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.', exclude=('*tests*',)),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'do-not-commit = pre_commit_hooks.do_not_commit.do_not_commit:main'
        ],
    },
)
