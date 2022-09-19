from random import randrange

# variant 1


def Find():
    print(len(set([randrange(1, 101) for i in range(30)])))


Find()


