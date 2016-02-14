from pair_debruijn.util import parse_gapped_patterns, string_spelled_by_gapped_patterns


def test_parse_gapped_patterns():
    lines = ['GACC|GCGC',
             'ACCG|CGCC',
             'CCGA|GCCG',
             'CGAG|CCGG',
             'GAGC|CGGA']

    expected = [('GACC', 'GCGC'),
                ('ACCG', 'CGCC'),
                ('CCGA', 'GCCG'),
                ('CGAG', 'CCGG'),
                ('GAGC', 'CGGA')]

    actual = parse_gapped_patterns(lines)

    assert (expected == actual)


def test_string_spelled_by_gapped_patterns():
    gapped_patterns = [('GACC', 'GCGC'),
                       ('ACCG', 'CGCC'),
                       ('CCGA', 'GCCG'),
                       ('CGAG', 'CCGG'),
                       ('GAGC', 'CGGA')]

    expected = 'GACCGAGCGCCGGA'

    actual = string_spelled_by_gapped_patterns(gapped_patterns, 4, 2)

    assert(expected == actual)
