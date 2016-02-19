from protein_translation import translate, transcribe


def test_translate():
    input = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    expected = 'MAMAPRTEINSTRING'
    actual = translate(input)

    assert (expected == actual)


def test_transcribe():
    input = 'ACGT'
    expected = 'ACGU'
    actual = transcribe(input)

    assert(expected == actual)
