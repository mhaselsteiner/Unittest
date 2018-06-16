from math import pi

def calc_cricle_area(r):
    if r < 0:
        raise ValueError('Accepts only positive real numbers as r!')
    if type(r) not in [int, float]:
        raise TypeError('Accepts only positive real numbers as r!')

    return pi * r ** 2

radii=[1,2.2, 2+3j, True, 'string', -2]

print(calc_cricle_area(1))
#[ print(calc_cricle_area(x)) for x in radii]