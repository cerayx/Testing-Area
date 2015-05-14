# -*- coding: utf-8 -*-
import math
import pprint


class MyPrettyPrinter(pprint.PrettyPrinter):

    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context,
                                           maxlevels, level)


def main(element):
    decimal, degree = math.modf(element)
    decimal_min = abs(round((decimal * 60), 3))
    sign = u"\u00B0"
    return u"{}{} {}'".format(int(degree), sign, decimal_min)


if __name__ == '__main__':
    coordinates = ((35.1559396703, -90.051861154),
                   (35.1556006047, -90.0452734708),
                   (35.1254266667, -89.9593513438),
                   (35.0620946957, -89.8413049881),
                   (35.0468400814, -90.0242124181),
                   (35.0463786042, -89.7646810742),
                   (35.1345278453, -90.0575200378),
                   (35.0979580489, -89.8516395905))
    for i in coordinates:
        print(map(main, i))
        MyPrettyPrinter().pprint(map(main, i))
        # verify output
