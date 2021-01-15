# Copyright 2015 Andy Tzeng <andytzeng@aol.tw>. All Rights Reserved.
# Licensed under BSD 3-Clause License.
import enum

from . import schemes
from ._regex import re
from .tlds import TLDs
from .tlds_pseudo import PseudoTLDs
from .unicode import otherPuncMinusDoubleQuote


def any_of(*args):
    return '({})'.format('|'.join([re.escape(p) for p in args]))


class URIPattern(enum.Enum):
    letter = r'\p{L}'
    mark = r'\p{M}'
    number = r'\p{N}'
    iri_char = letter + mark + number
    currency = r'\p{Sc}'
    other_symb = r'\p{So}'
    end_char = rf'{iri_char}/\-_+&~%=#{currency}{other_symb}'
    mid_char = rf'{end_char}_*{otherPuncMinusDoubleQuote}'
    well_paren = rf'\([{mid_char}]*(\([{mid_char}]*\)[{mid_char}]*)*\)'
    well_brack = rf'\[[{mid_char}]*(\[[{mid_char}]*\][{mid_char}]*)*\]'
    well_brace = rf'\{{[{mid_char}]*(\{{[{mid_char}]*\}}[{mid_char}]*)*\}}'
    well_all = rf'{well_paren}|{well_brack}|{well_brace}'
    path_cont = rf'([{mid_char}]*({well_all}|[{end_char}])+)+'

    iri = rf'[{iri_char}]([{iri_char}\-]*[{iri_char}])?'
    domain = rf'({iri}\.)+'
    octet = '(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])'
    ipv4_addr = rf'\b{octet}\.{octet}\.{octet}\.{octet}\b'
    ipv6_addr = r'([0-9a-fA-F]{1,4}:([0-9a-fA-F]{1,4}:([0-9a-fA-F]{1,4}:([0-9a-fA-F]{1,4}:([0-9a-fA-F]{1,4}:[0-9a-fA-F]{0,4}|:[0-9a-fA-F]{1,4})?|(:[0-9a-fA-F]{1,4}){0,2})|(:[0-9a-fA-F]{1,4}){0,3})|(:[0-9a-fA-F]{1,4}){0,4})|:(:[0-9a-fA-F]{1,4}){0,5})((:[0-9a-fA-F]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9a-fA-F]{1,4}:){1,6}|:):[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){7}:'
    ip_addr = rf'({ipv4_addr}|{ipv6_addr})'
    port = r'(:[0-9]*)?'


# ANY_SCHEME can be passed to strict_matching_scheme to match any possibly valid
# scheme, and not just the known ones.
ANY_SCHEME = r'([a-zA-Z][a-zA-Z.\-+]*://|{no_authority}:)'.format(no_authority=any_of(*schemes.NO_AUTHORITY))


def strict_exp():
    schemes_ptn = r'(({official}|{unofficial})://|{no_authority}:)'.format(
        official=any_of(*schemes.OFFICIAL),
        unofficial=any_of(*schemes.UNOFFICIAL),
        no_authority=any_of(*schemes.NO_AUTHORITY),
    )
    return rf'(?i:{schemes_ptn}){URIPattern.path_cont.value}'


def relaxed_exp():
    punycode = r'xn--[a-z0-9-]+'
    known_tlds = any_of(*(TLDs + PseudoTLDs))
    site = rf'{URIPattern.domain.value}(?i:({punycode}|{known_tlds}))'
    hostname = rf'({site}|{URIPattern.ip_addr.value})'
    web_url = rf'{hostname}{URIPattern.port.value}(/|/{URIPattern.path_cont.value})?'
    return rf'{strict_exp()}|{web_url}'


# strict_matching_scheme produces a regexp similar to Strict, but requiring that
# the scheme match the given regular expression. See AnyScheme too.
def strict_matching_scheme(exp):
    return rf'(?i:({exp})){URIPattern.path_cont.value}'
