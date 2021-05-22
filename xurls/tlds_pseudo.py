# Copyright 2021 Andy Tzeng <andytzeng@aol.tw>. All Rights Reserved.
# Licensed under BSD 3-Clause License.

# Refer the tool unicodegen from mvdan.cc/xurls/v2

# PseudoTLDs is a sorted list of some widely used unofficial TLDs.
#
# Sources:
#  * https://en.wikipedia.org/wiki/Pseudo-top-level_domain
#  * https://en.wikipedia.org/wiki/Category:Pseudo-top-level_domains
#  * https://tools.ietf.org/html/draft-grothoff-iesg-special-use-p2p-names-00
#  * https://www.iana.org/assignments/special-use-domain-names/special-use-domain-names.xhtml
PSEUDO_TLDS = [
    'bit',  # Namecoin
    'example',  # Example domain
    'exit',  # Tor exit node
    'gnu',  # GNS by public key
    'i2p',  # I2P network
    'invalid',  # Invalid domain
    'local',  # Local network
    'localhost',  # Local network
    'test',  # Test domain
    'zkey',  # GNS domain name
]
