import sys

def fileRead(filename)->list:
    file = open(filename, "r")
    lines = file.read()
    mas =[]
    for element in lines.split():
        mas.append(int(element))
    file.close()
    return mas

if __name__ == '__main__':
    if len(sys.argv) > 1:
        pathCircle = sys.argv[1]
    mas = fileRead(pathCircle)
    minVal = 10000000
    temp = 0
    for i in range(len(mas)):
        temp = 0
        for j in range(len(mas)):
            if i != j:
                temp += abs(mas[j]-mas[i])
        if temp < minVal:
            minVal = temp

    print(minVal)