#Convertion from Degrees Decimal Minutes to Decimal Degrees
Given a Degrees Decimal Minutes coordinate such as -90°03.11202W, convert it to a number of decimal degrees using the following method:
    (1) The integer number of degrees is the same (90)
    (2) The decimal degrees is the decimal minutes divided by 60
        (03.11202/60 = ~ .051867)
    (3) Sum of the two numbers 90 + .051867 = 90.051867)
    (4) For coordinates in the western or southern hemispheres, negate
        the result
    (5) The final result is -90.051867

From left to right in string:
    (1) convert leading zero hemisphere indicator to a negative sign (-)
    (2) convert first instance of whitespace to the degree sign (°)
    (3) remove any leading zero after whitespace
    (4) truncate/round int after decimal to three significant digits
    (5) convert directional to an apostrophe sign (') 