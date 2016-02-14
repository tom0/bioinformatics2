import contigs


def test_maximal_non_branching_paths():
    input = {1: [2],
             2: [3],
             3: [4, 5],
             6: [7],
             7: [6]}

    expected = [[1, 2, 3],
                [3, 4],
                [3, 5],
                [6, 7, 6]]

    actual = contigs.maximal_non_branching_paths(input)

    assert (expected == actual)
