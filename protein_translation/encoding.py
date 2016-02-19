from protein_translation import transcribe, translate
from util import reverse_complement


def encode(dna, peptide):
    rna = transcribe(dna)
    reverse_complement_rna = transcribe(reverse_complement(dna))
    rna_substr_len = len(peptide) * 3

    return [dna[i:i + rna_substr_len] for i in range(0, len(rna) - rna_substr_len + 1) if
            translate(rna[i:i + rna_substr_len]) == peptide or
            translate(reverse_complement_rna[len(rna) - (i + rna_substr_len):len(rna) - i]) == peptide]
