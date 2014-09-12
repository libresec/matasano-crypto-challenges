'''
http://cryptopals.com/sets/1/challenges/1/

The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206
20706f69736f6e6f7573206d757368726f6f6d

Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

Cryptopals Rule:
Always operate on raw bytes, never on encoded strings. Only use
hex and base64 for pretty-printing.

'''


def hex_to_base64(hex_string):
    return hex_string.decode("hex").encode("base64").strip()

if __name__ == "__main__":
    hex_string = '49276d206b696c6c696e6720796f757220627261696e206' \
        'c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print hex_to_base64(hex_string)
