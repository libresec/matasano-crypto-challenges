'''
http://cryptopals.com/sets/1/challenges/2/

Write a function that takes two equal-length buffers
and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:
746865206b696420646f6e277420706c6179
'''


def xor(s1, s2):
    result = "".join(chr(ord(x) ^ ord(y))
                     for x, y in zip(s1.decode("hex"), s2.decode("hex")))
    return result.encode("hex").strip()

if __name__ == "__main__":
    s1 = '1c0111001f010100061a024b53535009181c'
    s2 = '686974207468652062756c6c277320657965'
    print xor(s1, s2)
