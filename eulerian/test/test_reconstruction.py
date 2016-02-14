from eulerian.reconstruction import reconstruct


def test_reconstruct():
    kmers = ['CTTA',
             'ACCA',
             'TACC',
             'GGCT',
             'GCTT',
             'TTAC']

    expected = 'GGCTTACCA'

    text = reconstruct(kmers)

    assert (expected == text)
