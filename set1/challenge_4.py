'''
line: 7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f
 5(15) --> now that the party is jumping
'''
import challenge_3


def isprintable(s):
    try:
        s.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

if __name__ == "__main__":
    possible_solutions = []

    with open("challenge_4.txt") as f:
        for line in f:
            solution = challenge_3.break_single_char_xor(line.strip()).get_best_key()
            if isprintable(solution[2]):
                possible_solutions.append(solution)

    for s in possible_solutions:
        print s
