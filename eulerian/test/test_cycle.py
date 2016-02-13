import eulerian.cycle
import eulerian.util


def test_find_cycle():
    input = {
        0: [3],
        1: [0],
        2: [1, 6],
        3: [2],
        4: [2],
        5: [4],
        6: [5, 8],
        7: [9],
        8: [7],
        9: [6]}

    expected = [6, 5, 4, 2, 1, 0, 3, 2, 6, 8, 7, 9, 6]

    assert (expected == eulerian.cycle.find_cycle(input))


def test_find_cycle_with_loop():
    input = {
        0: [3],
        1: [3],
        2: [1],
        3: [2, 4],
        4: [0, 5],
        5: [7],
        6: [4],
        7: [6]}

    expected = [4, 0, 3, 2, 1, 3, 4, 5, 7, 6, 4]

    assert (expected == eulerian.cycle.find_cycle(input))


def test_find_cycle_with_multiple_loops():
    input = {
        0: [1, 4],
        1: [2],
        2: [3],
        3: [0],
        4: [5, 7],
        5: [6],
        6: [0, 12],
        7: [8, 10, 14, 16],
        8: [9],
        9: [4],
        10: [11],
        11: [7],
        12: [13],
        13: [6],
        14: [15],
        15: [7],
        16: [17],
        17: [7]
    }

    expected = [7, 8, 9, 4, 5, 6, 12, 13, 6, 0, 1, 2, 3, 0, 4, 7, 10, 11, 7, 14, 15, 7, 16, 17, 7]

    assert (expected == eulerian.cycle.find_cycle(input))
