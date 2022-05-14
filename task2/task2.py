import sys
from itertools import cycle
from math import *

def fileReadCircle(filename)->list:
    file = open(filename, "r")
    lines = file.read().replace('\n', ' ')
    k = lines.split()
    file.close
    return k

def fileReadPoints(filename)->dict:
    file = open(filename, "r")
    lines = file.readlines()
    dictPoint = {}
    for i in range(len(lines)):
        k = lines[i].split()
        dictPoint[i] = float(k[0]),float(k[1])
    file.close
    return dictPoint

def distance(x1, y1, x2, y2):
    dis = sqrt((x2-x1)**2 + (y2-y1)**2)
    return dis

if __name__ == '__main__':
    if len(sys.argv) > 1:
        pathCircle = sys.argv[1]
    if len(sys.argv) > 2:
        pathPoints = sys.argv[2]
    Circle = fileReadCircle(pathCircle)
    Xcirc = float(Circle[0])
    Ycirc = float(Circle[1])
    rad = float(Circle[2])
    Points = fileReadPoints(pathPoints)
    res = ""
    for i in range(len(Points)):
        dist = distance(Xcirc,Ycirc,Points[i][0],Points[i][1])**2 - rad**2
        if dist == 0:
            res += str(i) + " - точка лежит на окружности\n"
        elif dist < 0:
            res += str(i) + " - точка внутри\n"
        elif dist > 0:
            res += str(i) + " - точка снаружи\n"
    print(res)