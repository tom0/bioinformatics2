from eulerian.kuniversal import create_circular_string


def test_create_circular_string():
    expected = '0000110010111101'
    actual = create_circular_string(4)
    assert (expected == actual)
