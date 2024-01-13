from forbiddenfruit import curse


def words_of_wisdom(self):
    return self * "blah "


curse(int, "words_of_wisdom", words_of_wisdom)
print((2).words_of_wisdom())
