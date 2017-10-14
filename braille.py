#!/usr/bin/env python3

TYPE_HEX = 0
TYPE_ASCII = 1
TYPE_BINARY = 2
TYPE_BRAILLE = 3

with open('lookup_table.txt', 'r') as f:
    rows = f.read().splitlines()
table = list(map(lambda x: x.split('\t'), rows))


def convert(text_array, in_type=TYPE_BINARY, out_type=TYPE_ASCII, sep=''):
    output = []

    input_table = list(map(lambda x: x[in_type], table))
    output_table = list(map(lambda x: x[out_type], table))

    for item in text_array:
        index = input_table.index(item.upper())
        output.append(output_table[index])

    return sep.join(output)
