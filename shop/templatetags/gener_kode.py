import random
import string


def buildblock(size):
    return ''.join(random.choice(string.digits) for _ in range(size))
