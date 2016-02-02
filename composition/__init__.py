def composition(text, k):
    return [text[i:i + k] for i in range(len(text) - (k - 1))]

