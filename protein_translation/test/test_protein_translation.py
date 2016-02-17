from protein_translation import translate


def test_translate():
    input = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    expected = 'MAMAPRTEINSTRING'
    actual = translate(input)

    assert (expected == actual)
