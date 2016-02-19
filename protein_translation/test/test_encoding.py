from protein_translation.encoding import encode


def test_encode():
    dna = 'ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
    peptide = 'MA'

    expected = ['ATGGCC',
                'GGCCAT',
                'ATGGCC']

    actual = encode(dna, peptide)

    assert(expected == actual)
