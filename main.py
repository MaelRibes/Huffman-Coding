text = "Input a tdhbvsufyvgbehrjgvsybiuncsubrtusybfidnext : "


def get_frequencies(text):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


freq = get_frequencies(text)
frequencies_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print(frequencies_sorted)


def alpha_sort(freq):
    for k in range(len(freq)):
        for index in range(len(freq) - 1):
            freq1 = freq[index]
            freq2 = freq[index + 1]
            if freq1[1] == freq2[1]:
                if ord(freq1[0]) > ord(freq2[0]):
                    freq[index], freq[index + 1] = freq[index + 1], freq[index]
    return freq


print(alpha_sort(frequencies_sorted))
