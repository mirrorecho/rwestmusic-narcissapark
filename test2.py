



class Ship1(object):
    yo_mama="!!!"
    yo_papa="???"

    def __init__(self, yo=None, **kwargs):
        print("YO: ")
        print(yo)
        # print("ARGS: ")
        # print(args)
        print("KWARGS: ")
        print(kwargs)
        print("----------------------------------------------------")


class Ship2(Ship1):
    def __init__(self, **kwargs):
        print(blah)
        super().__init__(**kwargs)


s1 = Ship1("yo music here", bland="!")

s2 = Ship2("yo music here", bland="!")






