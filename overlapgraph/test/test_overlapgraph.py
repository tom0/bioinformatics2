import overlapgraph


def test_overlap_create():
    kmers = ['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT']
    expected = [('GCATG', 'CATGC'), ('CATGC', 'ATGCG'), ('AGGCA', 'GGCAT'), ('GGCAT', 'GCATG')]

    actual = overlapgraph.create(kmers)

    expected.sort()
    actual.sort()

    assert (expected == actual)
