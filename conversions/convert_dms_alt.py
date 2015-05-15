# coding=utf-8
import pyproj
import math
import os

def main(*coordinates):
    '''
    Purpose: Convert TN State Plane to degrees minitues sceconds.
    name: main()
    Parameters: main(lattitude, longitiude)
    '''
    def dms(element):
        decimal, degree = math.modf(element)
        decimal_min = abs(round((decimal * 60), 3))
        sign = u"\u00B0"
        return u"{}{} {}'".format(int(degree), sign, decimal_min)
    try:
        projections = {'WGS1984': pyproj.Proj("+init=EPSG:4326"),
                       'STATE': pyproj.Proj("+init=ESRI:102736", coordinates)}
        x, y = pyproj.transform(projections['STATE'],
                                projections['WGS1984'], *coordinates)
        return dms(x), dms(y)
    except ImportError:
        print 'Please install pyproj'


def test():
    points = ((819145.000051, 287838.250172),
              (757603.549971, 324495.6575),
              (774683.966926, 321640.753433),
              (841840.180382, 281230.999935),
              (764588.210215, 284146.74312))
    for x, y in points:
        print main(x, y)

if __name__ == '__main__':
    try:
        import arcpy
        address_data = os.path.join(r'C:\Users\carlt\Documents\ArcGIS'
                                    r'\Default.gdb', 'SHELBY', 'FIVE')

        with arcpy.da.UpdateCursor(address_data,
                                   ['SHAPE@X', 'SHAPE@Y', 'LON', 'LAT']) as cur:
            for row in cur:
                print main(row[0], row[1])
                row[2], row[3] = main(row[0], row[1])
                cur.updateRow(row)
    except ImportError, e:
        test()
        print 'arcpy not detected'