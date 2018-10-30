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
    # generate 2500 points
    numPoints = 6
    print('generating', numPoints, 'points...')
    points = generatePoints(numPoints)
    print('done')

    # generate unique lines
    print('generating lines...')
    lines, parallel = generateLines(points)
    print('done')

    numLines = len(lines)
    numParallel = len(parallel)

    print('total number of lines found =', numLines, 'number of parallel lines =', numParallel, 'for', numPoints, 'points')

    # count intersections

    end = timer()
    print('took', end - start, 'seconds')

def generateLines(points):
    lines = []
    parallel = []

    print('number of tests =', len(points) * (len(points) - 1))

    tests = 0

    for p1 in points:
        rest = points.copy()
        rest.remove(p1)

        for p2 in rest:
            tests += 1
            print('test', tests)
            pointsInLine = { p1, p2 }

            if (p2[0] - p1[0] == 0):
                slope = 'undefined'
            else:
                slope = (p2[1] - p1[1])/(p2[0] - p1[0])

            lineAlreadyFound = False

            for prevLine in lines:
                if any(elem in pointsInLine for elem in prevLine['points']):
                    if (slope == prevLine['slope']):
                        prevLine['points'] = prevLine['points'].union(pointsInLine)
                        lineAlreadyFound = True
                        break
                else:
                    if (slope == prevLine['slope']):
                        parallel.append({
                            'points': pointsInLine,
                            'slope': slope
                    })

            if (lineAlreadyFound is False):
                line = {
                    'points': pointsInLine,
                    'slope': slope
                }
                lines.append(line)
    return lines, parallel

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
