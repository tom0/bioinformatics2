import eulerian.path


def test_find_path_():
    input = {
        0: [2],
        1: [3],
        2: [1],
        3: [0, 4],
        6: [3, 7],
        7: [8],
        8: [9],
        9: [6]}

    expected = [6, 7, 8, 9, 6, 3, 0, 2, 1, 3, 4]

    assert (expected == eulerian.path.find_path(input))