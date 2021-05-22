# Copyright 2021 Andy Tzeng <andytzeng@aol.tw>. All Rights Reserved.
# Licensed under BSD 3-Clause License.
import pytest

import xurls


@pytest.fixture
def constant_cases():
    return [
        ('', None),
        (' ', None),
        (':', None),
        ('::', None),
        (':::', None),
        ('::::', None),
        ('.', None),
        ('..', None),
        ('...', None),
        ('1.1', None),
        ('.1.', None),
        ('1.1.1', None),
        ('1:1', None),
        (':1:', None),
        ('1:1:1', None),
        ('://', None),
        ('foo', None),
        ('foo:', None),
        ('mailto:', None),
        ('foo://', None),
        ('http://', None),
        ('http:// foo', None),
        ('http:// foo', None),
        (':foo', None),
        ('://foo', None),
        ('foorandom:bar', None),
        ('foo.randombar', None),
        ('zzz.', None),
        ('.zzz', None),
        ('zzz.zzz', None),
        ('/some/path', None),
        ('rel/path', None),
        ('localhost', None),
        ('com', None),
        ('.com', None),
        ('com.', None),
        ('http', None),
        ('http://foo', True),
        ('http://FOO', True),
        ('http://FAÀ', True),
        ('https://localhost', True),
        ('mailto:foo', True),
        ('MAILTO:foo', True),
        ('sms:123', True),
        ('xmpp:foo@bar', True),
        ('bitcoin:Addr23?amount=1&message=foo', True),
        ('cid:foo-32x32.v2_fe0f1423.png', True),
        ('mid:960830.1639@XIson.com', True),
        ('http://foo.com', True),
        ('http://foo.co.uk', True),
        ('http://foo.random', True),
        (' http://foo.com/bar ', 'http://foo.com/bar'),
        (' http://foo.com/bar more', 'http://foo.com/bar'),
        ('<http://foo.com/bar>', 'http://foo.com/bar'),
        ('<http://foo.com/bar>more', 'http://foo.com/bar'),
        ('.http://foo.com/bar.', 'http://foo.com/bar'),
        ('.http://foo.com/bar.more', 'http://foo.com/bar.more'),
        (',http://foo.com/bar,', 'http://foo.com/bar'),
        (',http://foo.com/bar,more', 'http://foo.com/bar,more'),
        ('*http://foo.com/bar*', 'http://foo.com/bar'),
        ('*http://foo.com/bar*more', 'http://foo.com/bar*more'),
        ('_http://foo.com/bar_', 'http://foo.com/bar_'),
        ('_http://foo.com/bar_more', 'http://foo.com/bar_more'),
        ('(http://foo.com/bar)', 'http://foo.com/bar'),
        ('(http://foo.com/bar)more', 'http://foo.com/bar'),
        ('[http://foo.com/bar]', 'http://foo.com/bar'),
        ('[http://foo.com/bar]more', 'http://foo.com/bar'),
        ("'http://foo.com/bar'", 'http://foo.com/bar'),
        ("'http://foo.com/bar'more", "http://foo.com/bar'more"),
        ('"http://foo.com/bar"', 'http://foo.com/bar'),
        ('"http://foo.com/bar"more', 'http://foo.com/bar'),
        ('{"url":"http://foo.com/bar"}', 'http://foo.com/bar'),
        ('{"before":"foo","url":"http://foo.com/bar","after":"bar"}', 'http://foo.com/bar'),
        ("http://a.b/a0/-+_&~*%=#@.,:;'?![]()a", True),
        ('http://a.b/a0/$€¥', True),
        ('http://✪foo.bar/pa✪th©more', True),
        ('http://foo.bar/path/', True),
        ('http://foo.bar/path-', True),
        ('http://foo.bar/path+', True),
        ('http://foo.bar/path&', True),
        ('http://foo.bar/path~', True),
        ('http://foo.bar/path%', True),
        ('http://foo.bar/path=', True),
        ('http://foo.bar/path#', True),
        ('http://foo.bar/path.', 'http://foo.bar/path'),
        ('http://foo.bar/path,', 'http://foo.bar/path'),
        ('http://foo.bar/path:', 'http://foo.bar/path'),
        ('http://foo.bar/path;', 'http://foo.bar/path'),
        ("'http://foo.bar/path'", 'http://foo.bar/path'),
        ('http://foo.bar/path?', 'http://foo.bar/path'),
        ('http://foo.bar/path!', 'http://foo.bar/path'),
        ('http://foo.bar/path@', 'http://foo.bar/path'),
        ('http://foo.bar/path|', 'http://foo.bar/path'),
        ('http://foo.bar/path|more', 'http://foo.bar/path'),
        ('http://foo.bar/path<', 'http://foo.bar/path'),
        ('http://foo.bar/path<more', 'http://foo.bar/path'),
        ('http://foo.com/path_(more)', True),
        ('(http://foo.com/path_(more))', 'http://foo.com/path_(more)'),
        ('http://foo.com/path_(even)-(more)', True),
        ('http://foo.com/path_(even)(more)', True),
        ('http://foo.com/path_(even_(nested))', True),
        ('(http://foo.com/path_(even_(nested)))', 'http://foo.com/path_(even_(nested))'),
        ('http://foo.com/path_[more]', True),
        ('[http://foo.com/path_[more]]', 'http://foo.com/path_[more]'),
        ('http://foo.com/path_[even]-[more]', True),
        ('http://foo.com/path_[even][more]', True),
        ('http://foo.com/path_[even_[nested]]', True),
        ('[http://foo.com/path_[even_[nested]]]', 'http://foo.com/path_[even_[nested]]'),
        ('http://foo.com/path_{more}', True),
        ('{http://foo.com/path_{more}}', 'http://foo.com/path_{more}'),
        ('http://foo.com/path_{even}-{more}', True),
        ('http://foo.com/path_{even}{more}', True),
        ('http://foo.com/path_{even_{nested}}', True),
        ('{http://foo.com/path_{even_{nested}}}', 'http://foo.com/path_{even_{nested}}'),
        ('http://foo.com/path#fragment', True),
        ('http://foo.com/emptyfrag#', True),
        ('http://foo.com/spaced%20path', True),
        ('http://foo.com/?p=spaced%20param', True),
        ('http://test.foo.com/', True),
        ('http://foo.com/path', True),
        ('http://foo.com:8080/path', True),
        ('http://1.1.1.1/path', True),
        ('http://1080::8:800:200c:417a/path', True),
        ('http://中国.中国/中国', True),
        ('http://中国.中国/foo中国', True),
        ('http://उदाहरण.परीकषा', True),
        ('http://xn-foo.xn--p1acf/path', True),
        ('what is http://foo.com?', 'http://foo.com'),
        ('go visit http://foo.com/path.', 'http://foo.com/path'),
        ('go visit http://foo.com/path...', 'http://foo.com/path'),
        ('what is http://foo.com/path?', 'http://foo.com/path'),
        ('the http://foo.com!', 'http://foo.com'),
        ('https://test.foo.bar/path?a=b', 'https://test.foo.bar/path?a=b'),
        ('ftp://user@foo.bar', True),
        ('http://foo.com/base64-bCBwbGVhcw==', True),
        ('http://foo.com/🐼', True),
        ('https://shmibbles.me/tmp/自殺でも？.png', True),
        ('randomtexthttp://foo.bar/etc', "http://foo.bar/etc"),
        ('postgres://user:pass@host.com:5432/path?k=v#f', True),
        ('postgres://user:pass@host.com:5432/path?k=v#f', True),
        ('zoommtg://zoom.us/join?confno=1234&pwd=xxx', True),
        ('zoomus://zoom.us/join?confno=1234&pwd=xxx', True),
    ]


def do_test(extractor, cases):
    for (input, expected) in cases:
        result = extractor.findfirst(input)

        if expected is True:
            expected = input

        assert result == expected


def test_strict_constant_cases(constant_cases):
    extractor = xurls.Strict()
    do_test(extractor, constant_cases)


def test_loosen_constant_cases(constant_cases):
    extractor = xurls.Relaxed()
    do_test(extractor, constant_cases)


def test_loosen_extra_cases():
    extractor = xurls.Relaxed()
    do_test(
        extractor,
        [
            ('foo.a', None),
            ('foo.com', True),
            ('foo.com bar.com', 'foo.com'),
            ('foo.com-foo', 'foo.com'),
            ('foo.company', True),
            ('foo.comrandom', None),
            ('some.guy', None),
            ('foo.example', True),
            ('foo.i2p', True),
            ('foo.local', True),
            ('foo.onion', True),
            ('中国.中国', True),
            ('中国.中国/foo中国', True),
            ('test.联通', True),
            ('test.联通 extra', 'test.联通'),
            ('test.xn--8y0a063a', True),
            ('test.xn--8y0a063a/foobar', True),
            ('test.xn-foo', None),
            ('test.xn--', None),
            ('foo.com/', True),
            ('1.1.1.1', True),
            ('10.50.23.250', True),
            ('121.1.1.1', True),
            ('255.1.1.1', True),
            ('300.1.1.1', None),
            ('1.1.1.300', None),
            ('foo@1.2.3.4', '1.2.3.4'),
            ('1080:0:0:0:8:800:200C:4171', True),
            ('3ffe:2a00:100:7031::1', True),
            ('1080::8:800:200c:417a', True),
            ('foo.com:8080', True),
            ('foo.com:8080/path', True),
            ('test.foo.com', True),
            ('test.foo.com/path', True),
            ('test.foo.com/path/more/', True),
            ('TEST.FOO.COM/PATH', True),
            ('TEST.FÓO.COM/PÁTH', True),
            ('foo.com/path_(more)', True),
            ('foo.com/path_(even)_(more)', True),
            ('foo.com/path_(more)/more', True),
            ('foo.com/path_(more)/end)', 'foo.com/path_(more)/end'),
            ('www.foo.com', True),
            (' foo.com/bar ', 'foo.com/bar'),
            (' foo.com/bar more', 'foo.com/bar'),
            ('<foo.com/bar>', 'foo.com/bar'),
            ('<foo.com/bar>more', 'foo.com/bar'),
            (',foo.com/bar.', 'foo.com/bar'),
            (',foo.com/bar.more', 'foo.com/bar.more'),
            (',foo.com/bar,', 'foo.com/bar'),
            (',foo.com/bar,more', 'foo.com/bar,more'),
            ('(foo.com/bar)', 'foo.com/bar'),
            ('"foo.com/bar\'', 'foo.com/bar'),
            ('"foo.com/bar\'more', 'foo.com/bar\'more'),
            ('"foo.com/bar"', 'foo.com/bar'),
            ('what is foo.com?', 'foo.com'),
            ('the foo.com!', 'foo.com'),
            ('foo@bar', None),
            ('foo@bar.a', None),
            ('foo@bar.com', "bar.com"),
            ('foo@sub.bar.com', "sub.bar.com"),
            ('foo@中国.中国', "中国.中国")
        ])


def test_strict_extra_cases():
    extractor = xurls.Strict()
    do_test(
        extractor, [
            ('http:// foo.com', None),
            ('foo.a', None),
            ('foo.com', None),
            ('foo.com/', None),
            ('1.1.1.1', None),
            ('3ffe:2a00:100:7031::1', None),
            ('test.foo.com:8080/path', None),
            ('foo@bar.com', None),
        ])


def test_strict_scheme():
    extractor = xurls.StrictScheme('https://')
    do_test(extractor, [
        ('http://foo.com', None),
        ('https://foo.com', 'https://foo.com'),
        ('foo.com', None),
    ])


def test_nostrict_scheme():
    extractor = xurls.StrictScheme(xurls.express.ANY_SCHEME)
    do_test(
        extractor, [
            ('http://foo.com', 'http://foo.com'),
            ('https://foo.com', 'https://foo.com'),
            ('custom://foo.com', 'custom://foo.com'),
            ('foo.com', None),
        ])
