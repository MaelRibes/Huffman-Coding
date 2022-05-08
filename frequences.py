def get_frequencies(text):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return alpha_sort(frequencies)


def alpha_sort(f):
    freq = sorted(f.items(), key=lambda x: x[1])
    for k in range(len(freq)):
        for index in range(len(freq) - 1):
            freq1 = freq[index]
            freq2 = freq[index + 1]
            if freq1[1] == freq2[1]:
                if ord(freq1[0]) > ord(freq2[0]):
                    freq[index], freq[index + 1] = freq[index + 1], freq[index]
    res = tuplelist_to_dict(freq)
    return res


def tuplelist_to_dict(li):
    di = {}
    for tu in li:
        di[tu[0]] = tu[1]
    return di