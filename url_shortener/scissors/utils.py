import string
import random


def random_characters(length=5):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
