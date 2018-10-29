#!/usr/bin/env python3

# L = set of UNIQUE lines
# M(L) = number of lines in the set
# S(L) = sum over every line of the number of times that line is crossed by another line in the set

# points = (T2k-1, t2k) for integers k >= 1.
# (T1, T2), (T3, T4), (T5, T6), etc
# generated from:
# S0 = 290797
# Sn+1 = Sn2 mod 50515093
# Tn = ( Sn mod 2000 ) - 1000

# Ln = set of UNIQUE lines generated from joining every point in a set of n points. The lines are extended indefinitely in both directions.

# Find S(L2500)

##############################################################################################################################################

# Sum of touches in x UNIQUE NONPARALLEL lines = x(x-1)

import math
from timeit import default_timer as timer

def main():
    start = timer()
    # generate 25000 points
    numPoints = 200
    print('generating', numPoints, 'points...')
    points = generatePoints(numPoints)
    print('done')

    # generate unique lines
    print('generating lines...')
    lines = generateLines(points)
    print('done')

    numLines = len(lines)

    print('number of lines found =', numLines, 'for', numPoints)

    # remove nonparallel lines

    # count intersections

    end = timer()
    print('took', end - start, 'seconds')

def generateLines(points):
    lines = []

    print('number of tests =', len(points) * (len(points) - 1))

    for p1 in points:
        rest = points.copy()
        rest.remove(p1)

        for p2 in rest:
            pointsInLine = [ p1, p2 ]

            if (p2[0] - p1[0] == 0):
                slope = 'undefined'
            else:
                slope = (p2[1] - p1[1])/(p2[0] - p1[0])

            lineAlreadyFound = False

            for prevLine in lines:
                if(any(elem in pointsInLine for elem in prevLine['points']) and slope == prevLine['slope']):
                    for p in pointsInLine:
                        if (p not in prevLine['points']):
                            prevLine['points'].append(p)
                            # print('adding point to old line', prevLine['points'])
                    lineAlreadyFound = True
                    break

            if (lineAlreadyFound is False):
                line = {
                    'points': pointsInLine,
                    'slope': slope
                }
                # print('adding new line', line)
                lines.append(line)
    return lines

def generatePoints(numOfPoints):
    points = []
    origin = 290797

    while(len(points) < numOfPoints):
        if (len(points) is 0):
            y = origin

        x = getNext(y)
        y = getNext(x)

        points.append((x, y))

    return convertToT(points)

def getNext(prev):
    next = (prev ** 2) % 50515093
    return next

def convertToT(listOfPoints):
    convertedPoints = []
    for point in listOfPoints:
        x = ( point[0] % 2000 ) - 1000
        y = ( point[1] % 2000 ) - 1000
        convertedPoints.append((x, y))
    return convertedPoints

if __name__ == "__main__":
  main()
