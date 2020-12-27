# PyXURLs

[![PyPI version](https://badge.fury.io/py/pyxurls.svg)](https://badge.fury.io/py/pyxurls)
[![Build Status](https://travis-ci.com/andytzeng/pyxurls.svg?branch=main)](https://travis-ci.com/andytzeng/pyxurls)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyxurls)

A regular expression based URL extractor which extracts URLs from text.

Thanks to [Daniel Martí](https://github.com/mvdan) invests the project [mvdan/xurls](https://github.com/mvdan/xurls). This python project developed by the same concept as the golang version.

## Installing

```bash
pip install pyxurls
```

## Usage

### Extract URLs by strict strategy

```python
import xurls

extractor = xurls.Strict()

url = extractor.findfirst('we have the link with scheme https://www.python.org and https://www.github.com')
#  https://www.python.org

urls = extractor.findall('we have the link with scheme https://www.python.org and https://github.com')
#  ['https://www.python.org', 'https://github.com']
```

### Extract URLs by relaxed strategy

```python
import xurls

extractor = xurls.Relaxed()

url = extractor.findfirst('we have the link with scheme www.python.org and https://www.github.com')
#  www.python.org

urls = extractor.findall('we have the link with scheme www.python.org and https://github.com')
#  ['www.python.org', 'https://github.com']
```

### Extract URLs by limit scheme

```python
import xurls

# limit to https
extractor = xurls.StrictScheme('https://')

url = extractor.findfirst('we have the link with scheme custom://domain.com and https://www.python.org noscheme.com')
#  https://www.python.org

# unlimit to standard scheme
extractor = xurls.StrictScheme(xurls.express.ANY_SCHEME)
urls = extractor.findall('we have the link with scheme custom://domain.com and https://www.python.org noscheme.com')
#  ['custom://domain.com', 'https://www.python.org']
```
