def reverse_complement(pattern):
    complements = {
        'G': 'C',
        'A': 'T',
        'C': 'G',
        'T': 'A'
    }
    return ''.join([complements[p] for p in pattern][::-1])
