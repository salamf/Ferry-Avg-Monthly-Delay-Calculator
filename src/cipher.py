#!/usr/bin/env python3


class DecryptException(Exception):
    pass


def decode_line(alphabet, line, key):
    """ Decrypts an encrypted string, and returns the result """

    res = ""
    for index, letter in enumerate(line):
        line_char_val = alphabet.index(letter)
        key_char_val = alphabet.index(key[index % len(key)])

        letter_pos = (line_char_val - key_char_val) % len(alphabet)

        res += alphabet[letter_pos]

    return res


def check_str(lis):
    """ Checks if the decrypted information was decrypted properly """

    return '!' and '@' and '#' and '$' and '%' and '^' and '&' and '*' and '(' and ')' \
           and '-' and '_' and '+' and '=' and '~' and '`' and '{' and '}' and '[' and ']' \
           and '\\' and ';' and ':' and '"' and "'" and '/' and '?' and '<' and '>' \
           and '.' and '|' not in ''.join(lis)


class FileDecoder(object):
    """ FileDecoder iterable class """

    def __init__(self, key, filename, alphabet):
        self.key = key
        self.filename = filename
        self.alphabet = alphabet
        whole_str = self.open()
        self.header_line = whole_str[0].split(',')
        self.input_string = whole_str[1:]

    def open(self):
        with open(self.filename, 'r') as input_file:
            try:
                whole_str = decode_line(self.alphabet, input_file.read(), self.key).splitlines()

                if not check_str(whole_str):
                    raise DecryptException from None

            except Exception:
                raise DecryptException from None

        return whole_str

    def __repr__(self):
        return "FileDecoder(key='{}', file='{}')".format(self.key, self.filename)

    def __len__(self):
        return len(self.input_string) + 1

    def __iter__(self):
        for line in self.input_string:
            yield line.split(',')
