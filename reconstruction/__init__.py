def reconstruct(kmers):
    if not kmers:
        return ''
    temp = [kmer[0] for kmer in kmers[:-1]]
    temp.append(kmers[-1])
    return ''.join(temp)

