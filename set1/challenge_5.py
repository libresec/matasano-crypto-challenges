'''
http://cryptopals.com/sets/1/challenges/5/

Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the
first byte of plaintext will be XOR'd against I, the next C, the next E,
then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt
your mail. Encrypt your password file. Your .sig file. Get a feel for it.
I promise, we aren't wasting your time with this.

'''

import challenge_2


class repeating_key_xor:

    def __init__(self, key, plaintext):
        self.exp_key = self.expand_key(key.encode("hex"),
                                       len(plaintext.encode("hex")))
        self.get_xor()

    def expand_key(self, key, length_plaintext):
        quotient, remainder = divmod(length_plaintext, len(key))
        return (key * quotient) + key[:remainder]

    def get_xor(self):
        return challenge_2.xor(plaintext.encode("hex"), self.exp_key)


if __name__ == '__main__':
    plaintext = "Burning 'em, if you ain't quick and nimble " \
        "I go crazy when I hear a cymbal"
    key = "ICE"

    print repeating_key_xor(key, plaintext).get_xor()
