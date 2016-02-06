def composition(text, k):
    return [text[i:i + k] for i in range(len(text.strip()) - (k - 1))]

