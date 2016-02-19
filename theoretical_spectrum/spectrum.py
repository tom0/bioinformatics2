from theoretical_spectrum import weights


def generate(peptide):
    spectrum = []
    double_peptide = peptide + peptide
    for n in range(1, len(peptide)):
        spectrum += [double_peptide[i:i + n] for i in range(0, len(peptide))]

    spectrum.append(peptide)

    res = [0] + [sum([weights[c] for c in s]) for s in spectrum]
    res.sort()
    return res
