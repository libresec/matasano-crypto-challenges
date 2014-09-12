from bitstring import BitArray
from itertools import izip
import distance


class break_repeating_key_xor:

    def __init__(self, ciphertext, keysizes):
        self.ciphertext = ciphertext
        self.keysizes = keysizes

    def get_hamming_distance(self, string1, string2):
        if len(string1) == len(string2):
            s1_b = BitArray(hex=string1.encode("hex"))
            s2_b = BitArray(hex=string2.encode("hex"))
            return distance.hamming(s1_b, s2_b)

    def get_hamming_distance_hard_way(self, string1, string2):
        if len(string1) == len(string2):
            s1 = ''.join(format(ord(x), 'b').zfill(8) for x in string1)
            s2 = ''.join(format(ord(x), 'b').zfill(8) for x in string2)
            return sum(c1 != c2 for c1, c2 in izip(s1, s2))

    def get_best_edit_dist(self):
        best_edit_dist = {}
        for keysize in self.keysizes:
            first_chunk = ciphertext[:keysize]
            second_chunk = ciphertext[keysize:keysize * 2]
            edit_dist = self.get_hamming_distance(
                first_chunk, second_chunk)
            best_edit_dist[keysize] = edit_dist / float(keysize)
        best_key = min(best_edit_dist, key=best_edit_dist.get)
        best_key_value = min(best_edit_dist.itervalues())
        return best_key, best_key_value


if __name__ == '__main__':
    # 2 - Sanity check. Hamming Distance should be 37
    # s1 = "this is a test"
    # s2 = "wokka wokka!!!"
    # print break_repeating_key_xor().get_hamming_distance(s1, s2)
    # print break_repeating_key_xor().get_hamming_distance_hard_way(s1, s2)

    # 3 - For each KEYSIZE, take the first KEYSIZE worth of bytes, and
    # the second KEYSIZE worth of bytes, and find the edit distance between
    # them. Normalize this result by dividing by KEYSIZE.

    with open('challenge_6.txt') as f:
        data = f.readlines()

    ciphertext = ''.join(data).strip().encode("hex")
    keysizes = range(1, 41)
    b = break_repeating_key_xor(ciphertext, keysizes)

    print b.get_best_edit_dist()
