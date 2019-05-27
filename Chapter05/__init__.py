from Chapter05 import Example5_8 as ex58

if __name__ == '__main__' :
    bingo = ex58.BingoCage(range(6))
    print(bingo.pick())
    print(bingo())
    print(bingo())
    print(callable(bingo))