import sys
import heapq


def file_character_frequencies(file_name):
    file = open(file_name, 'r')
    file_content = file.read();
    freq = {}
    for i in file_content:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one using double parens e.g. PriorityTuple((x, (y, z))) """

    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]

    def __gt__(self, other):
        return self[0] > other[0]

    def __ge__(self, other):
        return self[0] >= other[0]

    def __eq__(self, other):
        return self[0] == other[0]

    def __ne__(self, other):
        x = self.__eq__(other)
        return not x


def huffman_codes_from_frequencies(frequencies):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]

    heapq.heapify(heap)

    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    a = convert(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))
    return a


def convert(ls):
    return dict(ls)


def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    # Suggested strategy...
    freqs = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freqs)


def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))


def main():
    """Provided to help you play with your code."""
    import pprint
    frequencies = file_character_frequencies(sys.argv[1])
    pprint.pprint(frequencies)
    codes = huffman_codes_from_frequencies(frequencies)
    pprint.pprint(codes)
    encode_file_using_codes("example.txt", codes)
    decode_file_using_codes("example.txt_encoded", codes)


if __name__ == '__main__':
    main()
