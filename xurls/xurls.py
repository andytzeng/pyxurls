# Copyright 2015 Andy Tzeng <andytzeng@aol.tw>. All Rights Reserved.
# Licensed under BSD 3-Clause License.
from . import express
from ._regex import LONEST_MATCH, re


class Base(object):

    pattern = None

    def __init__(self):
        if not self.pattern:
            raise ValueError('invalid pattern')

        self.re_url = re.compile(self.pattern, LONEST_MATCH)

    def findfirst(self, string):
        match = self.re_url.search(string)
        if match:
            return match.group()

    def findall(self, string):
        return [x.group() for x in self.re_url.finditer(string)]


class Strict(Base):
    pattern = express.strict_exp()


class Relaxed(Base):
    pattern = express.relaxed_exp()


class StrictScheme(Base):

    def __init__(self, scheme_exp):
        self.pattern = express.strict_matching_scheme(scheme_exp)
        super().__init__()
