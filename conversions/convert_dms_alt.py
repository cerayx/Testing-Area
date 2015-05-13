# -*- coding: utf-8 -*-
'''
Given a Degrees Decimal Minutes coordinate such as -90°03.11202W, convert it to a number of decimal degrees using the following method:
    (1) The integer number of degrees is the same (90)
    (2) The decimal degrees is the decimal minutes divided by 60 (03.11202/60 = ~ .051867)
    (3) Sum of the two numbers 90 + .051867 = 90.051867)
    (4) For coordinates in the western or southern hemispheres, negate the result
    (5) The final result is -90.051867

from left to right in string: 
    (1) convert leading zero hemisphere indicator to a negative sign (-)
    (2) convert first instance of whitespace to the degree sign (°)
    (3) remove any leading zero after whitespace
    (4) truncate/round int after decimal to three significant digits
    (5) convert directional to an apostrophe sign (') '''

def main(x):
    z = str(x[1]).split('.')

    print z

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
        main(i)
