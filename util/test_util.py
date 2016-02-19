from util import reverse_complement


def test_reverse_complement():
    input = 'ACGT'
    expected = 'ACGT'
    actual = reverse_complement(input)

    assert (expected == actual)
