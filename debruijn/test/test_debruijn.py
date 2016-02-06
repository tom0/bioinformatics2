import debruijn


def test_create():
    k = 4
    text = 'AAGATTCTCTAAGA'

    expected = {'AAG': ['AGA', 'AGA'], 'TCT': ['CTC', 'CTA'], 'GAT': ['ATT'], 'AGA': ['GAT'], 'ATT': ['TTC'],
                'CTA': ['TAA'], 'CTC': ['TCT'], 'TTC': ['TCT'], 'TAA': ['AAG']}
    actual = debruijn.create(text, k)

    assert (expected == actual)


def test_create_from_patterns():
    patterns = ['GAGG', 'CAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']

    expected = {'AGG': ['GGG'], 'CAG': ['AGG', 'AGG'], 'GAG': ['AGG'], 'GGA': ['GAG'], 'GGG': ['GGG', 'GGA']}
    actual = debruijn.create_from_patterns(patterns)

    assert (expected == actual)
