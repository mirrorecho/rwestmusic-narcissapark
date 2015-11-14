



class Ship1(object):
    yo_mama="!!!"
    yo_papa="???"

    class Meta:
        color="Blue"
        number=1


class Ship2(Ship1):
    class Meta:
        number=2


s = Ship2()

print(s.Meta.color)