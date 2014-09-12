'''
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt
the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character
frequency is a good metric. Evaluate each output and choose the one with the
best score.
'''


class break_single_char_xor(object):

    def __init__(self, ciphertext):
        self.keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
            'abcdefghijklmnopqrstuvwxyz0123456789'
        self.ciphertext = ciphertext
        self.most_frequent = 'etaionsh'
        self.freq_count = {}
        self.possible_solutions = {}
        self.solve_for_keys()

    def solve_for_keys(self):
        for key in self.keys:
            result = "".join(chr(ord(x) ^ ord(key))
                             for x in self.ciphertext.decode("hex"))
            result = result.strip(' ').lower()
            self.possible_solutions[key] = result
            self.freq_count[key] = 0
            for letter in self.most_frequent:
                self.freq_count[key] += result.count(letter)

    def get_best_key(self):
        best_key = max(self.freq_count, key=self.freq_count.get)
        best_key_value = max(self.freq_count.itervalues())
        return (best_key, best_key_value, self.possible_solutions[best_key])


if __name__ == "__main__":
    ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d36'\
        '3c78373e783a393b3736'
    print break_single_char_xor(ciphertext).get_best_key()
