from composition import composition


def test_composition_splits_into_kmers():
    text = 'CAATCCAAC'
    k = 5

    kmers = composition(text, k)
    assert kmers == ['CAATC', 'AATCC', 'ATCCA', 'TCCAA', 'CCAAC']


def test_composistion_all_kmers_k_length():
    text = 'CTGAAGACCTCTCCACATTACTACGATATAAATCATTTCAGCCTCTAGATACGCCTTGGTGGGTGGGGTTGGCAATTTACGATATGTCCGAATGATTTGACACCAAATACCTTAGCTAGCCCCAAGGAAAATTCTGGGCTTTACGTTGGCCGAGCCACATTACTACAGTAAGGTTAAGCAACCAGCCAGTCGCTCATAAGGACTCCACGCCTCCCGTTACTGACTTCCAACAACAATGTGACAGTAGACTGGAACCTGGGAGGACATTATTGATTCGCCGCGAATCTTCTAAGGTATTTTACCCCCACTGGTCACCTTAACCATTAAGACCTCGAAGTGACACCTAGCCTCTTAACACCCAACTCCACCGACAATACCTATTCGCTGACAAGCGGGACATCCGATCGCCCCTGACTCGAGGTGTCTACCGTCCATCGATTGCTAAACTTTGTTAGGAGTCTAAGCGAACCATGGGAAGGGGGCGGCAGTCAACGTGCTCCTTTAGTGAGGTACCATATTCTTACAGCATGTGGAGCGCAGCAAACTAGCGACCGGGAGTACTCCCACAACCCTGGGTACGTACTGCACTTTTTTCAAGAGCCAGGGTCATTTAAATAGCATCTTTGCTCTTTCTGATAAGGGGGCGACCATCTCCGAATTGAGCCAAACGCTGGTATAAGACTCGTCTCATGACTCCCTAGCCATTTGTATGTTGTCATTTCTGATTTTAGCAGGTAAAACGTAAGGCCTGCTAAAGAATCACGCGGGGAGGCCTTAAATTTCGTCATGGAGCAATCGTCCTAGATTGCTGTGAAGGTTCGTACCAGTAGAGTCTAATGTGCGTAAATGTTAACTGGCCGTATATTCTCTGGTGAGCTGAAACAGAAAGCTGGCAGAAAGCCACTCTTGCTGTTTCGTGTGTACGGACATCGGGATAGTACCAAAAAGCATGTTCTTCATCTGGCGATGCTTGATGTCTACCGTAGACACCTTCATACGT '
    kmers = composition(text, 12)

    for kmer in kmers:
        assert (12 == len(kmer))
