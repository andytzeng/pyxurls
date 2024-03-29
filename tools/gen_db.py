import codecs
import csv
import re
import urllib.request

import click

SCHEME_CSV = 'https://www.iana.org/assignments/uri-schemes/uri-schemes-1.csv'

COPYRIGHT = '''# Copyright 2021 Andy Tzeng <andytzeng@aol.tw>. All Rights Reserved.
# Licensed under BSD 3-Clause License.

# Refer the tool unicodegen from mvdan.cc/xurls/v2
# Generated by gen_db.py
'''

SCHEME_TMPL = f'''{COPYRIGHT}
# Schemes is a sorted list of all IANA assigned schemes.
# Official Scheme from the IANA:
#   https://www.iana.org/assignments/uri-schemes/uri-schemes-1.csv
OFFICIAL = [
{{schemes}}
]

UNOFFICIAL = [
    'jdbc',  # Java database Connectivity
    'postgres',  # PostgreSQL (short form)
    'postgresql',  # PostgreSQL
    'slack',  # Slack
    'zoommtg',  # Zoom (desktop)
    'zoomus',  # Zoom (mobile)
]

# No Authority schemes is a sorted list of some well-known url schemes that are
# followed by ":" instead of "://". The list includes both officially
# registered and unofficial schemes.
NO_AUTHORITY = [
    'bitcoin',  # Bitcoin
    'cid',  # Content-ID
    'file',  # Files
    'magnet',  # Torrent magnets
    'mailto',  # Mail
    'mid',  # Message-ID
    'sms',  # SMS
    'tel',  # Telephone
    'xmpp',  # XMPP
]'''

TLDS_TMPL = f'''{COPYRIGHT}
# TLDs is a sorted list of all public top-level domains.
# Sources:
#   * https://data.iana.org/TLD/tlds-alpha-by-domain.txt
#   * https://publicsuffix.org/list/effective_tld_names.dat
ASCII_TLDS = [
{{ascii_tlds}}
]

NON_ASCII_TLDS = [
{{non_ascii_tlds}}
]'''


def gen_scheme():
    with urllib.request.urlopen(SCHEME_CSV) as fp:
        reader = csv.DictReader(codecs.iterdecode(fp, 'utf-8'))

        schemes = ['    \'{}\','.format(row['URI Scheme']) for row in reader]

    print(SCHEME_TMPL.format(schemes='\n'.join(schemes)))


def fetch_tlds(url, ptn):
    with urllib.request.urlopen(url) as fp:
        data = fp.read().decode('utf-8')

    lter = (v.group() for v in re.finditer(ptn, data, re.MULTILINE))
    return {v.lower() for v in lter if not v.startswith('XN--')}


def gen_tlds():
    s1 = fetch_tlds('https://data.iana.org/TLD/tlds-alpha-by-domain.txt', r'^[^#\n]+$')
    s2 = fetch_tlds('https://publicsuffix.org/list/effective_tld_names.dat', r'^[^/.\n]+$')
    tlds = list(sorted(s1 | s2))

    ascii_tlds, non_ascii_tlds = [], []
    for i, tld in enumerate(tlds):
        if not tld[0].isascii():
            ascii_tlds = ['    \'{}\','.format(v) for v in tlds[:i]]
            non_ascii_tlds = ['    \'{}\','.format(v) for v in tlds[i:]]
            break

    print(TLDS_TMPL.format(
        ascii_tlds='\n'.join(ascii_tlds),
        non_ascii_tlds='\n'.join(non_ascii_tlds),
    ))


@click.command()
@click.argument('target', required=True)
def main(target):
    """Tool to generate the scheme or TLDs based om the live database
    The available `target` can be `scheme` and `tlds`
    """
    if target == 'scheme':
        gen_scheme()
    elif target == 'tlds':
        gen_tlds()
    else:
        raise ValueError('invalid target')


if __name__ == '__main__':
    main()
