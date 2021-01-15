try:
    # re2 will be first choose
    import re2 as re  # NOQA

    LONEST_MATCH = re.Options()
    LONEST_MATCH.longest_match = True
except ImportError:
    import regex as re  # NOQA

    LONEST_MATCH = re.POSIX
