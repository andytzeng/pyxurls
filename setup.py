from os import path

import setuptools

_no_re2, _no_regex = False, False

try:
    import re2 as re  # NOQA
except ImportError:
    _no_re2 = True


try:
    import regex as re  # NOQA
except ImportError:
    _no_regex = True

if _no_re2 and _no_regex:
    import warnings
    warnings.warn('re2 or regex not installed. Please install either re2 or regex as engine')


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='pyxurls',
    version='0.1.2',
    author='Andy Tzeng',
    author_email='andytzeng@aol.tw',
    description='A regular expression based URL extractor which extracts URLs from text.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andytzeng/pyxurls',
    packages=setuptools.find_namespace_packages(include=['xurls']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='url regex extract',
    python_requires='>=3.6',
)
