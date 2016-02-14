import kmer_reconstruction


def parse_gapped_patterns(gapped_pattern_lines):
    res = []
    for line in gapped_pattern_lines:
        parts = line.split('|')
        res.append((parts[0], parts[1]))
    return res


def string_spelled_by_gapped_patterns(gapped_patterns, k, d):
    first_patterns = [gp[0] for gp in gapped_patterns]
    second_patterns = [gp[1] for gp in gapped_patterns]

    prefix_string = kmer_reconstruction.reconstruct(first_patterns)
    suffix_string = kmer_reconstruction.reconstruct(second_patterns)

    for i in range(k + d + 1, len(prefix_string)):
        p = prefix_string[i]
        s = suffix_string[i - k - d]
        if p != s:
            return None

    return prefix_string + suffix_string[-(k + d):]
