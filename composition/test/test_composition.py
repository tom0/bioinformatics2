from composition import composition


def test_composition_splits_into_kmers():
    text = 'CAATCCAAC'
    k = 5

    kmers = composition(text, k)
    assert kmers == ['CAATC', 'AATCC', 'ATCCA', 'TCCAA', 'CCAAC']
