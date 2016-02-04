from reconstruction import reconstruct


def test_normal_case():
    kmers = ['ACCGA', 'CCGAA', 'CGAAG', 'GAAGC', 'AAGCT']
    expected = 'ACCGAAGCT'
    assert (expected == reconstruct(kmers))


def test_single_kmer():
    kmers = ['ACCGA']
    expected = 'ACCGA'
    assert (expected == reconstruct(kmers))


def test_single__char_kmers():
    kmers = ['A', 'C', 'C', 'G', 'A']
    expected = 'ACCGA'
    assert (expected == reconstruct(kmers))


def test_empty_kmers():
    kmers = []
    expected = ''
    assert (expected == reconstruct(kmers))
