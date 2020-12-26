import setuptools

setuptools.setup(
    name='xurls',
    version='0.1.0',
    author='Andy Tzeng',
    author_email='andytzeng@aol.tw',
    description='Extract URLs from text',
    url='https://github.com/andytzeng/xurls',
    packages=setuptools.find_namespace_packages(include=['xurls']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'regex',
    ],
    python_requires='>=3.6',
)
