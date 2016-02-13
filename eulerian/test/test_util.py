import eulerian.cycle
import eulerian.util


def test_parse_edges():
    input_lines = ['0 -> 3', '1 -> 0', '2 -> 1,6', '3 -> 2', '4 -> 2', '5 -> 4', '6 -> 5,8', '7 -> 9', '8 -> 7',
                   '9 -> 6']

    expected = {
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

    assert (expected == eulerian.util.parse_edges(input_lines))


def test_cycle_to_string():
    input = [6, 5, 4, 2, 1, 0, 3, 2, 6, 8, 7, 9, 6]
    expected = '6->5->4->2->1->0->3->2->6->8->7->9->6'
    assert (expected == eulerian.util.to_string(input))