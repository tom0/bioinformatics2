from theoretical_spectrum.spectrum import generate


def test_generate():
    input = 'LEQN'
    expected = [0, 113, 114, 128, 129, 227, 242, 242, 257, 355, 356, 370, 371, 484]

    actual = generate(input)

    assert (expected == actual)
