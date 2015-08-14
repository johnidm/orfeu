import random
import string

class Util:

    @staticmethod
    def random_string(length):
        return ''.join(random.choice(string.ascii_letters) for x in range(length))

    @staticmethod
    def random_range_string(start, end):
        length = random.randrange(start, end)
        return Util.random_string(length)
